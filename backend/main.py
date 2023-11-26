import json
import math
import random
import time
import uuid

import uvicorn
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import shutil
from pathlib import Path
import pandas as pd

from dg import DG
from dg_reader import read_dg_excel
from isc import ISC
import db

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
isc = ISC()


@app.post("/uploadxlsx/")
async def upload_xlsx(name: str, file: UploadFile = File(...)):
    filepath = Path("uploads") / (name + ".xlsx")  # str(uuid.uuid4())
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    jsons = read_dg_excel(filepath)
    for payload in jsons:
        payload["extension"].append({"url": "https://BiopsyID.com", "valueString": name})
        print("upload status code", isc.post("/Observation", payload))

    # insert into additionals
    dgs = DG.get_for_biopsy_id(isc, name)
    for dg in dgs:
        db.create_dg_additional({
            "phir_id": dg.id,
            "class": None,
            "filename": name,
            "biopsy_id": dg.biopsy_id,
        })

    db.create_biopsy(db.Biopsy({
        "biopsy_id": name,
        "dg_phir_ids": [dg.id for dg in dgs],
    }))

    return JSONResponse(status_code=200, content={"message": "File uploaded and read into DataFrame successfully"})


@app.post("/upload")
async def upload_test():
    path = "../EHH23_Icebreaker_AZ23/DG/DG-14013-23-1A_S1 (paired)_Filtered_variants_DNA.xlsx"
    jsons = read_dg_excel(path)
    for payload in jsons:
        print("upload status code", isc.post("/Observation", payload))
    return 200


@app.get("/observations")
async def read_obs():
    return isc.get("/Observation")


@app.get("/patients")
async def get_patients():
    return isc.get("/Patient")


@app.post("/patients")
async def post_patients():
    data = isc.post("/Patient", {
        "resourceType": "Patient",
        "name": [{"family": "Smith"}]
    })
    return True


@app.get("/dg")
async def get_dg():
    data = isc.get("/Observation")
    dgs = []
    for dg_data in data["entry"]:
        dgs.append(DG.from_fhir(dg_data))

    adds = [dg.find_additionals(db.dg_additionals_table) for dg in dgs]

    resp_data = {"dg": [{**dg.as_json(), "class": adds[i]["class"]} for i, dg in enumerate(dgs)]}
    return JSONResponse(status_code=200, content=resp_data)


@app.get("/dg/{biopsy_id}")
async def get_dg_biopsy(biopsy_id: str):
    data = isc.get("/Observation")
    dgs = []
    for dg_data in data["entry"]:
        dg = DG.from_fhir(dg_data)
        if dg.biopsy_id == biopsy_id:
            dgs.append(dg)

    adds = [dg.find_additionals(db.dg_additionals_table) for dg in dgs]

    resp_data = {"dg": [{**dg.as_json(), "class": adds[i]["class"]} for i, dg in enumerate(dgs)]}
    return JSONResponse(status_code=200, content=resp_data)


@app.post("/classify_dg")
async def classify_dg(phir_id: int, classification: str):
    phir_id = str(phir_id)
    db.classify_dg(phir_id, classification)


@app.get("/biopsy")
async def get_biopsy():
    return db.biopsy_table.all()


@app.post("/biopsy/{biopsy_id}")
async def post_biopsy(biopsy_id: str, data: dict):
    biopsy = db.Biopsy.from_id(biopsy_id)
    for key in data:
        assert key in db.BIOPSY_KEYS, f"Unknown key {key} used in biopsy update"
        setattr(biopsy, key, data[key])
    biopsy.update_db()

@app.get("/geneDanger")
def get_gene_danger():
    dgs = isc.get("/Observation")
    dgs = [DG.from_fhir(dg) for dg in dgs["entry"]]
    adds = [dg.find_additionals(db.dg_additionals_table) for dg in dgs]
    for i, add in enumerate(adds):
        if add["class"] is None:
            adds[i]["class"] = random.choice(["Benign", "Pathogenic"])
    data = [{"id": dg.id, "name": dg.gene_name, "class": add["class"]} for dg, add in zip(dgs, adds)]
    def count_classes(data):
        result = {}
        for item in data:
            name = item['name']
            class_type = item['class']
            if name not in result:
                result[name] = {'name': name, 'n_safe': 0, 'n_dangerous': 0, "id": item["id"]}
            if class_type == 'Benign':
                result[name]['n_safe'] += 1
            elif class_type == 'Pathogenic':
                result[name]['n_dangerous'] += 1
        return list(result.values())

    counts = count_classes(data)
    counts = [{"freq": str(round(100*count["n_dangerous"]/(count["n_safe"] + count["n_dangerous"]))) + "%", **count} for count in counts]
    return sorted(counts, key=lambda x: x["n_dangerous"], reverse=True)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

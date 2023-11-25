import json
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

    resp_data = {"dg": [dg.as_json() for dg in dgs]}
    return JSONResponse(status_code=200, content=resp_data)


@app.get("/dg/{biopsy_id}")
async def get_dg_biopsy(biopsy_id: str):
    data = isc.get("/Observation")
    dgs = []
    for dg_data in data["entry"]:
        dg = DG.from_fhir(dg_data)
        if dg.biopsy_id == biopsy_id:
            dgs.append(dg)

    resp_data = {"dg": [dg.as_json() for dg in dgs]}
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
    biopsy = db.Biopsy(data)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

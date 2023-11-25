import json
import uuid

import uvicorn
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
from pathlib import Path
import pandas as pd

from dg_reader import read_dg_excel
from isc import ISC

app = FastAPI()
isc = ISC()


@app.post("/uploadxlsx/")
async def upload_xlsx(file: UploadFile = File(...)):
    file_location = Path("uploads") / str(uuid.uuid4())
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    df = pd.read_excel("../EHH23_Icebreaker_AZ23/DG/DG-14013-23-1A_S1 (paired)_Filtered_variants_DNA.xlsx")

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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

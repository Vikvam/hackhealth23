import db
from dg import DG
from dg_reader import read_dg_excel
from isc import ISC

isc = ISC()

fixture = [
    {"name": "DG-14013-23-1A_S1",
     "path": "../EHH23_Icebreaker_AZ23/DG/DG-14013-23-1A_S1 (paired)_Filtered_variants_DNA.xlsx"},
    {
        "path": "../EHH23_Icebreaker_AZ23/DG/DG-14338-23-plasma-UMI_S10 (paired)_Filtered_variants_DNA.xlsx",
        "name": "DG-14338-23-plasma-UMI_S10"
    },
    {
        "path": "../EHH23_Icebreaker_AZ23/DG/DG-1-122764-21-j-UMI_S11 (paired)_Filtered_variants_DNA.xlsx",
        "name": "DG-1-122764-21-j-UMI_S11"
    },
    {
        "path": "../EHH23_Icebreaker_AZ23/DG/DG-13217-23-1G_S2 (paired)_Filtered_variants_DNA.xlsx",
        "name": "DG-13217-23-1G_S2"
    }
]


def upload_xlsx(name: str, filepath):
    jsons = read_dg_excel(filepath)
    for payload in jsons:
        payload["extension"].append({"url": "https://BiopsyID.com", "valueString": name})
        print("upload status code", isc.post("/Observation", payload))

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

if __name__ == '__main__':
    for fix in fixture:
        upload_xlsx(fix["name"], fix["path"])

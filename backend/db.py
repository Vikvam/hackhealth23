from tinydb import TinyDB, Query

db = TinyDB("db.json")

# Schemas
# DG_additional = {
#    "phir_id": str,
#    "class": str, (green, yellow, red)
#    "filename": str,
#    "biopsy": Optional[int] (doc_id)
# }
#
# Biopsy = {
#   "id": int,
#   "dg": list[int] (phir_id)
#   "projekt": str,
#   "diagnoza": str,
#   "onkologicky_kod": str,
#   "kod_pojistovna": str,
#   "prijem_lmp": str,
#   "uzavreni_lmp": str,
#   "patient_id": str,
#   "igv_kontrola": str,
#   "medea_zapis": str,
#   "sekvenator": str,
#   "panel_genu": str,
#   "procento_nadorovych_bunek": str,
#   "DNA konc. po 1.PCR": str,
#   "DNA průměrné pokrytí": str,
#   "DNA TMB": str,
#   "DNA MSI": str,
#   "HRD": str,
#   "Genom build - původní": str,
# }
#

biopsy_table = db.table("biopsy")
dg_additionals_table = db.table("dg_class")


def create_biopsy(biopsy: dict, dg_phir_ids: list[str]):
    doc_ids = []
    DG_Add = Query()
    for phir_id in dg_phir_ids:
        search_results = db.search(DG_Add.phir_id == phir_id)
        assert len(search_results) != 0, f"Phir id {phir_id} not found in database"
        doc_ids.append(search_results[0].doc_id)

    biopsy["dg"] = doc_ids
    biopsy_table.insert(biopsy)


def create_dg_additional(dg_additional: dict):
    dg_additionals_table.insert(dg_additional)


def classify_dg(phir_id: str, classification: str):
    if len(dg_additionals_table.search(Query().phir_id == phir_id)) == 0:
        dg_additionals_table.insert({
            "phir_id": phir_id,
            "class": classification
        })
    dg_additionals_table.update({"class": classification}, Query().phir_id == phir_id)


if __name__ == '__main__':
    User = Query()
    print(db.search(User.age > 22))

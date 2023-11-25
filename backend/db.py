from tinydb import TinyDB, Query

db = TinyDB("db.json")

# Schemas
# DG_additional = {
#    "phir_id": str,
#    "class": str, (green, yellow, red)
#    "filename": str,
#    "biopsy_id": str
# }
#
# Biopsy = {
#   "biopsy_id": str,
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

BIOPSY_KEYS = [
    "biopsy_id",
    "dg_phir_ids",
    "projekt",
    "diagnoza",
    "onkologicky_kod",
    "kod_pojistovna",
    "prijem_lmp",
    "uzavreni_lmp",
    "patient_id",
    "igv_kontrola",
    "medea_zapis",
    "sekvenator",
    "panel_genu",
    "procento_nadorovych_bunek",
    "dna_konc_po_1_pcr",
    "dna_prum_pokryti",
    "dna_tmb",
    "dna_msi",
    "hrd",
    "genom_build_puvodni"
]


class Biopsy:
    def __init__(self, data: dict):
        for key in BIOPSY_KEYS:
            setattr(self, key, data.get(key, None))

    def as_json(self):
        json_data = {}
        for key in BIOPSY_KEYS:
            json_data[key] = getattr(self, key)
        return json_data


biopsy_table = db.table("biopsy")
dg_additionals_table = db.table("dg_class")


def create_biopsy(biopsy: Biopsy):
    biopsy_table.insert(biopsy.as_json())


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

import json

import numpy as np
import pandas as pd


def add_extension(element_name, possible_keys, row_dict, json_data):
    found_value = "unknown"
    for key in possible_keys:
        if key in row_dict:
            found_value = row_dict[key]
            break
    json_data["extension"].append({"url": f"https://{element_name}.com".replace(" ", ""), "valueString": str(found_value)})

def read_dg_excel(path):
    # Read all sheets of the Excel file into a dictionary of DataFrames
    all_sheets = pd.read_excel(path, sheet_name=None)
    jsons = []

    # Iterate over each sheet
    for sheet_name, df in all_sheets.items():
        # Convert each row to a dictionary and append it to a list
        df = df.replace({np.nan: None})
        data = []
        for index, row in df.iterrows():
            data.append(row.to_dict())

        for row_dict in data:
            json_data = {"resourceType": "Observation", "extension": []}
            with open('config.json', 'r') as config_file:
                config_data = json.load(config_file)
                for key, aliases in config_data.items():
                    add_extension(key, aliases, row_dict, json_data)

            json_data["status"] = "final"
            jsons.append(json_data)

    return jsons


if __name__ == "__main__":
    excel_file_path = '../EHH23_Icebreaker_AZ23/DG/DG-14013-23-1A_S1 (paired)_Filtered_variants_DNA.xlsx'
    print(read_dg_excel(excel_file_path))

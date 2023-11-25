import numpy as np
import pandas as pd


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

        # Convert the list of dictionaries to JSON
        # jsons.append({'extension': [{"url": i, "valueString": str(dat)} for i, dat in enumerate(data)]})
        for row_dict in data:
            json_data = {"coordinateSystem": 1, "extension": []}
            for key, value in row_dict.items():
                json_data["extension"].append({"url": f"https://{key}.com".replace(" ", ""), "valueString": str(value)})
            jsons.append(json_data)

    return jsons


if __name__ == "__main__":
    excel_file_path = '../EHH23_Icebreaker_AZ23/DG/DG-14013-23-1A_S1 (paired)_Filtered_variants_DNA.xlsx'

    print(read_dg_excel(excel_file_path))

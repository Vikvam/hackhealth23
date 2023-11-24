import pandas as pd


if __name__ == "__main__":
    excel_file_path = '../EHH23_Icebreaker_AZ23/DG/DG-14013-23-1A_S1 (paired)_Filtered_variants_DNA.xlsx'

    # Read all sheets of the Excel file into a dictionary of DataFrames
    all_sheets = pd.read_excel(excel_file_path, sheet_name=None)

    # Iterate over each sheet
    for sheet_name, df in all_sheets.items():
        # Convert each row to a dictionary and append it to a list
        data = []
        for index, row in df.iterrows():
            data.append(row.to_dict())

        # Convert the list of dictionaries to JSON
        json_data = {'extension': data}

        # Print or save the JSON data for each sheet
        print(f"JSON data for sheet '{sheet_name}': {json_data}")

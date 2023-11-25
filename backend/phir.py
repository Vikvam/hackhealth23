def get_extension_obj(data, ext_name: str):
    data = data["extension"]
    parsed_ext_name = ext_name.replace(" ", "").lower()
    for extension in data:
        curr_ext_name = extension["url"].replace("https://", "").replace(".com", "").lower()
        if curr_ext_name == parsed_ext_name:
            return extension
    print(f"WARN: {ext_name} not found in fhir data")

def get_extension_value(data, ext_name: str):
    ext_obj = get_extension_obj(data, ext_name)
    if ext_obj is None:
        return "None"
    return get_extension_obj(data, ext_name)["valueString"]


if __name__ == '__main__':
    data = [
        {
            "url": "https://Chromosome.com",
            "valueString": "10"
        }, {
            "url": "https://CodingChange.com",
            "valueString": "ABAB"
        }]

    print(get_extension_value(data, "Coding Change"))

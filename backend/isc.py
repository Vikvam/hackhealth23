import requests


class ISC:
    API_KEY = "ew2DuI4xtb2VrsMhTaFNc2Coqm1EImvS58emoGRT"
    url = "https://fhir.pzyj0rab8imc.workload-nonprod-fhiraas.isccloud.io"

    def get(self, endpoint):
        print("Url is", self.url + endpoint)
        response = requests.get(
            self.url + endpoint,
            headers={"x-api-key": self.API_KEY})
        print("Response", response)
        return response.json()

    def post(self, endpoint, payload):
        if isinstance(payload, str):
            return requests.post(
                self.url + endpoint,
                data=payload,
                headers={
                    "x-api-key": self.API_KEY,
                    "accept": "application/fhir+json",
                    "Content-Type": "application/fhir+json",
                }
            ).json()
        elif isinstance(payload, dict):
            return requests.post(
                self.url + endpoint,
                json=payload,
                headers={
                    "x-api-key": self.API_KEY,
                    "accept": "application/fhir+json",
                    "Content-Type": "application/fhir+json",
                }
            ).json()
        else:
            assert False, f"Invalid type for payload {type(payload)}"

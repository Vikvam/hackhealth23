import requests


class ISC:
    API_KEY = "DFA5QxMVgg1QFzD385wwY6Lkj9t4jsST36A2BEQi"
    url = "https://fhir.pzyj0rab8imc.workload-nonprod-fhiraas.isccloud.io"

    def get(self, endpoint):
        print("Url is", self.url + endpoint)
        response = requests.get(
            self.url + endpoint,
            headers={"x-api-key": self.API_KEY})
        return response.json()

    def post(self, endpoint, payload):
        if isinstance(payload, str):
            data = requests.post(
                self.url + endpoint,
                data=payload,
                headers={
                    "x-api-key": self.API_KEY,
                    "accept": "application/fhir+json",
                    "Content-Type": "application/fhir+json",
                }
            )
            return data.status_code
        elif isinstance(payload, dict):
            data = requests.post(
                self.url + endpoint,
                json=payload,
                headers={
                    "x-api-key": self.API_KEY,
                    "accept": "application/fhir+json",
                    "Content-Type": "application/fhir+json",
                }
            )
            return data.status_code
        else:
            assert False, f"Invalid type for payload {type(payload)}"

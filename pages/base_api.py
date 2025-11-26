import requests

class APIClient:
    def __init__(self, base_url):
        # Remove trailing slash only
        self.base_url = base_url.rstrip("/")

    def _handle_response(self, response):
        """Common response validation & parsing"""
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print("HTTP error:", err)
        except ValueError:
            print("Invalid JSON response")
        return None

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params, headers=headers)
        return self._handle_response(response)

    def post(self, endpoint, data=None, json_body=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, data=data, json=json_body, headers=headers)
        return self._handle_response(response)

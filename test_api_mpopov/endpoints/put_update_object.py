from test_api_mpopov.endpoints.base_endpoint import Endpoint
import requests
import allure


class PutObject(Endpoint):
    @allure.step("Update object")
    def make_changes_in_object(self, object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f"{self.url}/{object_id}", json=body, headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step("Checking to get the name 'color' object")
    def check_correct_data(self, title):
        assert self.json["data"]["color"] == title

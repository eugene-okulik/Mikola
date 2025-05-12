import requests
import allure
from test_api_mpopov.endpoints.base_endpoint import Endpoint


class CreateThreeObjects(Endpoint):
    @allure.step("Create three objects")
    def create_new_objects(self, body):
        self.response = requests.post(self.url,
                                      json=body,
                                      headers=self.headers)
        self.json = self.response.json()
        return self.response

    @allure.step("Checking get name objects")
    def check_body_name(self, name):
        assert self.json["name"] == name

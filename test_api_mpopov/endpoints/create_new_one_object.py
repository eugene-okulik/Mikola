import allure
import requests
from test_api_mpopov.endpoints.base_endpoint import Endpoint


class CreateOneObject(Endpoint):
    @allure.step("Create one object")
    def create_new_objects_id(self, body):
        self.response = requests.post(self.url,
                                      json=body,
                                      headers=self.headers)
        allure.attach(
            self.response.text,
            name="Response body",
            attachment_type=allure.attachment_type.JSON,
        )
        self.object_id = self.response.json()["id"]
        print("Create new object")
        return self.object_id

    @allure.step("Output object id")
    def print_result_object_data(self):
        print(self.object_id)

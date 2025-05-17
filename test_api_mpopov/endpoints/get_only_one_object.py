from test_api_mpopov.endpoints.base_endpoint import Endpoint
import allure
import requests


class GetOneObject(Endpoint):
    @allure.step("Launching a request to get one the object")
    def get_one_object(self, object_id):
        self.response = requests.get(f"{self.url}/{object_id}")
        allure.attach(
            self.response.text,
            name="Response body",
            attachment_type=allure.attachment_type.JSON,
        )
        self.object_id = self.response.json()["id"]

    @allure.step("Check object id found")
    def check_id_object(self, obj_id):
        assert self.object_id == obj_id

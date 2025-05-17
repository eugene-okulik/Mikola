from test_api_mpopov.endpoints.base_endpoint import Endpoint
import allure
import requests


url = "http://167.172.172.115:52353/object"


class DeleteObjects(Endpoint):
    @allure.step("Deleting an object by its ID")
    def delete_objects(self, obj_id):
        self.response = requests.delete(f"{url}/{obj_id}")

    @allure.step("Text print about deletion")
    def print_text_delete(self):
        print("Object deleted")

    @allure.step("Check delete response text")
    def check_response_text(self, expected_text):
        assert self.response.text == expected_text
        print(expected_text)

    @allure.step("Status code")
    def correspondence(self):
        assert self.response.reason == "OK"
        print(f"Corresponding to the status code 200: {self.response.reason}")

from test_api_mpopov.endpoints.base_endpoint import Endpoint
import allure
import requests


url = "http://167.172.172.115:52353/object"


class DeleteObjects(Endpoint):
    @staticmethod
    @allure.step("Deleting an object by its ID")
    def delete_objects(obj_id):
        requests.delete(f"{url}/{obj_id}")

    @staticmethod
    @allure.step("Text print about deletion")
    def print_text_delete():
        print("Object deleted")

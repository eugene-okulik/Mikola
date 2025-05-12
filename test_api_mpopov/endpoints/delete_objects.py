from test_api_mpopov.endpoints.base_endpoint import Endpoint
import allure
import requests


class DeleteObjects(Endpoint):

    @allure.step('Deleting an object by its ID')
    def delete_objects(self, object_id):
        self.response = requests.delete(
            f"{self.url}/{object_id}"
        )
        return self.response

    @allure.step('Text print about deletion')
    def print_text_delete(self):
        print('Object deleted')

    @allure.step('Print')
    def print_status_code(self):
        print(self.response.status_code)
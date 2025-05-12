from test_api_mpopov.endpoints.base_endpoint import Endpoint
import allure
import requests


class PatchObject(Endpoint):

    @allure.step('Getting an object based on test data')
    def patch_object(self, body, object_id):
        self.response = requests.patch(f'{self.url}/{object_id}',
                                       json=body,
                                       headers=self.headers)
        self.json = self.response.json()
        return self.response
from test_api_mpopov.endpoints.base_endpoint import Endpoint
import allure
import requests

class GetAllObjects(Endpoint):

    @allure.step('Launching a request to get all the objects')
    def get_all_objects(self):
        self.response = requests.get(url=self.url)
        allure.attach(str(self.response.status_code),
                      name='Status code',
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(self.response.text,
                      name='Response body',
                      attachment_type=allure.attachment_type.JSON)
        return self.response

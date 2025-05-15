import allure


class Endpoint:
    url = "http://167.172.172.115:52353/object"
    response = None
    json = None
    headers = {
        "Content-type": "application/json",
    }
    object_id = None

    @allure.step("Checking object to status code 200")
    def check_code_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step("Get object data output")
    def print_result_objects(self, obj_id):
        print(obj_id)

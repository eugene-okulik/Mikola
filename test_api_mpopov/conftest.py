import pytest
import allure
import requests
from test_api_mpopov.endpoints.create_add_objects import AddObjects
from test_api_mpopov.endpoints.put_update_object import PutObject
from test_api_mpopov.endpoints.get_full_all_objects import GetAllObjects
from test_api_mpopov.endpoints.get_only_one_object import GetOneObject
from test_api_mpopov.endpoints.delete_objects import DeleteObjects
from test_api_mpopov.endpoints.putch_a_object import PatchObject


headers = {
    "Content-type": "application/json",
}
url = "http://167.172.172.115:52353/object"
BODY = {
    "data": {"color": "Blue", "size": "very big"},
    "name": "new project",
}


@allure.step("Create one object")
@pytest.fixture()
def new_object_id(delete):
    response = requests.post(url, json=BODY, headers=headers)
    allure.attach(
        response.text,
        name="Response body",
        attachment_type=allure.attachment_type.JSON,
    )
    object_id = response.json()["id"]
    print("Create new object")
    yield object_id
    delete.delete_objects(object_id)
    delete.print_text_delete()


@pytest.fixture()
def start_completed_func():
    print("Start testing")
    yield
    print(30 * "-")
    print("Testing completed")


@pytest.fixture()
def before_after_func():
    print("before test")
    yield
    print("after test")


@pytest.fixture()
def all_objects():
    return GetAllObjects()


@pytest.fixture()
def one_object():
    return GetOneObject()


@pytest.fixture()
def delete():
    return DeleteObjects()


@pytest.fixture()
def create_additional_objects():
    return AddObjects()


@pytest.fixture()
def update_object():
    return PutObject()


@pytest.fixture()
def patch():
    return PatchObject()

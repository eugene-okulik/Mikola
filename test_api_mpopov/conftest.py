import pytest
from test_api_mpopov.endpoints.create_objects import CreateThreeObjects
from test_api_mpopov.endpoints.create_new_one_object import CreateOneObject
from test_api_mpopov.endpoints.update_object import PutObject
from test_api_mpopov.endpoints.get_all_the_objects import GetAllObjects
from test_api_mpopov.endpoints.get_one_the_object import GetOneObject
from test_api_mpopov.endpoints.delete_objects import DeleteObjects
from test_api_mpopov.endpoints.putch_a_object import PatchObject


@pytest.fixture()
def start_completed_func():
    print("Start testing")
    yield
    print(30 * '-')
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
def create_add_object():
    return CreateThreeObjects()


@pytest.fixture()
def create_new_object_id():
    return CreateOneObject()


@pytest.fixture()
def update_object():
    return PutObject()


@pytest.fixture()
def patch():
    return PatchObject()

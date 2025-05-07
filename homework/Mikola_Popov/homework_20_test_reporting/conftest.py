import pytest
import requests
from test_dir_19_task2.test_19 import test_delete_object


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
def create_new_object_id():
    body = {
        "data": {
            "color": "Blue",
            "size": "very big"
        },
        "name": "new project",
    }
    headers = {
        "Content-type": "application/json",
    }
    response = requests.post('http://167.172.172.115:52353/object',
                             json=body,
                             headers=headers).json()
    object_id = response['id']
    print(f"Created new object {object_id}")
    yield object_id
    test_delete_object(object_id)

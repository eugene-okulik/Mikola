import pytest
import requests


@pytest.fixture(scope='session')
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
def create_new_post_id():
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
    post_id = response['id']
    print(f"Created new object {post_id}")
    yield post_id
    requests.delete(f"http://167.172.172.115:52353/object/{post_id}")
    print("Post deleted")


def test_all_posts(start_completed_func, before_after_func):
    response = requests.get('http://167.172.172.115:52353/object')
    return response


@pytest.mark.medium
def test_one_post(before_after_func):
    response = requests.get('http://167.172.172.115:52353/object/1').json()
    print(response)


@pytest.mark.critical
@pytest.mark.parametrize('color, size, name',
                         [
                             ("yellow", "center", "Third object"),
                             ("Green", "medium", "Fourth object"),
                             ("White", "small", "Fifth object"),
                         ])
def test_add_post(color, size, name, before_after_func):
    body = {
        "data": {
            "color": color,
            "size": size
        },
        "name": name,
    }
    headers = {
        "Content-type": "application/json",
    }
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers)
    print(response.json())
    assert response.status_code == 200


def test_put_a_post(create_new_post_id, before_after_func):
    body = {
        "data": {
            "color": "black_and_white",
            "size": "too big"
        },
        "name": "current object",
    }
    headers = {
        "Content-type": "application/json; charset=UTF-8",
    }
    response = requests.put(
        f'http://167.172.172.115:52353/object/{create_new_post_id}',
        json=body,
        headers=headers)
    assert response.status_code == 200


def test_patch_a_post(create_new_post_id, before_after_func):
    body = {
        "data": {
            "color": "black_and_white",
            "size": "too big",
            "scale": "world"
        }
    }
    headers = {
        "Content-type": "application/json; charset=UTF-8",
    }
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{create_new_post_id}',
        json=body,
        headers=headers)
    assert response.status_code == 200

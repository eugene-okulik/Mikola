import pytest
import requests
import allure


@allure.feature('Objects')
@allure.story('Get objects')
@allure.title('Тест-функция для получения всех объектов')
def test_all_objects(start_completed_func, before_after_func):
    with allure.step('Launching a request to get all the objects'):
        response = requests.get('http://167.172.172.115:52353/object')
        allure.attach(str(response.status_code),
                      name='Status code',
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text,
                      name='Response body',
                      attachment_type=allure.attachment_type.JSON)
    with allure.step('Checking to get the status code objects 200'):
        assert response.status_code == 200


@allure.feature('Object')
@allure.story('Get one object')
@allure.title('Тест-функция для получения одного объекта')
@pytest.mark.medium
def test_one_object(before_after_func):
    with allure.step('Launching a request to get one the object'):
        response = requests.get('http://167.172.172.115:52353/object/1')
        allure.attach(response.text,
                      name='Response body',
                      attachment_type=allure.attachment_type.JSON)
    with allure.step('Output of the result of getting a sing object'):
        print(response.json())


@allure.feature('Objects')
@allure.story('Manipulate with objects')
@allure.title('Тест с параметризацией для создание трёх объектов')
@pytest.mark.critical
@pytest.mark.parametrize('color, size, name',
                         [
                             ("yellow", "center", "Third object"),
                             ("Green", "medium", "Fourth object"),
                             ("White", "small", "Fifth object"),
                         ])
def test_add_object(color, size, name, before_after_func):
    with allure.step('Preparation of test data'):
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
    with allure.step('Getting an object based on test data'):
        response = requests.post(
            'http://167.172.172.115:52353/object',
            json=body,
            headers=headers)
    with allure.step('Full object data output'):
        print(response.json())
    with allure.step('Checking to get the status code objects 200'):
        assert response.status_code == 200


@allure.feature('Objects')
@allure.story('Delete objects')
@allure.title('Функция для удаления объектов')
def test_delete_object(create_new_object_id):
    with allure.step('Deleting an object by its ID'):
        requests.delete(
            f"http://167.172.172.115:52353/object/{create_new_object_id}"
        )
    with allure.step('Text print about deletion'):
        print("Object deleted")


@allure.feature('Request')
@allure.story('Put object')
@allure.title('Тест-функция изменение объкта')
def test_put_a_object(create_new_object_id, before_after_func):
    with allure.step('Preparation of test data for object modification'):
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
    with allure.step('Getting an object based on test data'):
        response = requests.put(
            f'http://167.172.172.115:52353/object/{create_new_object_id}',
            json=body,
            headers=headers)
    with allure.step('Checking to get the status code objects 200'):
        assert response.status_code == 200


@allure.feature('Request')
@allure.story('Patch object')
@allure.title('Тест-функция изменение неких значений(строк)')
def test_patch_a_post(create_new_object_id, before_after_func):
    with allure.step('Preparation of test data for parameter changes'):
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
    with allure.step('Getting an object based on test data'):
        response = requests.patch(
            f'http://167.172.172.115:52353/object/{create_new_object_id}',
            json=body,
            headers=headers)
    with allure.step('Checking to get the status code objects 200'):
        assert response.status_code == 200

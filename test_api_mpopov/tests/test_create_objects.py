import allure
import pytest


def test_all_objects(all_objects, start_completed_func, before_after_func):
    all_objects.get_all_objects()
    all_objects.check_code_status()


def test_get_one_object(one_object, before_after_func):
    one_object.get_one_object(1)
    one_object.print_result_objects()


@pytest.mark.parametrize('color, size, name',
                         [
                             ("yellow", "center", "Third object"),
                             ("Green", "medium", "Fourth object"),
                             ("White", "small", "Fifth object"),
                         ])
def test_add_object(color, size, name, create_add_object, before_after_func):
    with allure.step('Preparation of test data'):
        body = {
            "data": {
                "color": color,
                "size": size
            },
            "name": name,
        }
    create_add_object.create_new_objects(body)
    create_add_object.print_result_objects()
    create_add_object.check_body_name(body['name'])
    create_add_object.check_code_status()


BODY = {
    "data": {
        "color": "Blue",
        "size": "very big"
    },
    "name": "new project",
}


def test_one_new_object_id(create_new_object_id):
    create_new_object_id.create_new_objects_id(BODY)
    create_new_object_id.print_result_object_data()


def test_delete_object(delete, create_new_object_id):
    delete.delete_objects(create_new_object_id.create_new_objects_id(BODY))
    delete.check_code_status()
    delete.print_status_code()
    delete.print_text_delete()


def test_put_a_object(create_new_object_id, update_object, before_after_func, delete):
    with allure.step('Preparation of test data for object modification'):
        body = {
            "data": {
                "color": "black_and_white",
                "size": "too big"
            },
            "name": "current object",
        }
    obj_id = create_new_object_id.create_new_objects_id(BODY)
    update_object.make_changes_in_object(obj_id, body=body)
    update_object.check_correct_data(body['data']['color'])
    update_object.check_code_status()
    delete.delete_objects(update_object.make_changes_in_object(obj_id, body=body))
    delete.print_text_delete()



def test_patch_a_post(patch, create_new_object_id, delete, before_after_func):
    with allure.step('Preparation of test data for parameter changes'):
        body = {
            "data": {
                "color": "black_and_white",
                "size": "too big",
                "scale": "world"
            }
        }
    obj_id = create_new_object_id.create_new_objects_id(BODY)
    patch.patch_object(body, obj_id)
    patch.check_code_status()
    patch.print_result_objects()
    delete.delete_objects(patch.patch_object(body, obj_id))
    delete.print_text_delete()

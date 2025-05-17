import allure
import pytest


def test_all_objects(all_objects, start_completed_func, before_after_func):
    all_objects.get_all_objects()
    all_objects.check_code_status_is_200()


def test_get_one_object(one_object, new_object_id, before_after_func):
    one_object.get_one_object(new_object_id)
    one_object.check_id_object(new_object_id)


@pytest.mark.parametrize(
    "color, size, name",
    [
        ("yellow", "center", "Third object"),
        ("Green", "medium", "Fourth object"),
        ("White", "small", "Fifth object"),
    ],
)
def test_add_object(color, size, name, create_additional_objects,
                    before_after_func):
    with allure.step("Preparation of test data"):
        body = {
            "data": {"color": color, "size": size},
            "name": name,
        }
    create_additional_objects.create_add_objects(body)
    create_additional_objects.print_result_objects(
        create_additional_objects.create_add_objects(body)
    )
    create_additional_objects.check_body_name(body["name"])


def test_delete_object(delete, new_object_id):
    delete.delete_objects(new_object_id)
    delete.print_text_delete()
    delete.check_response_text(
        f"Object with id {new_object_id} successfully deleted"
    )
    delete.correspondence()


def test_put_a_object(new_object_id, update_object, before_after_func):
    with allure.step("Preparation of test data for object modification"):
        body = {
            "data": {"color": "black_and_white", "size": "too big"},
            "name": "current object",
        }
    object_id = new_object_id
    update_object.make_changes_in_object(object_id, body=body)
    update_object.check_correct_data(body["data"]["color"])
    update_object.check_code_status_is_200()


def test_patch_a_post(patch, new_object_id, delete, before_after_func):
    with allure.step("Preparation of test data for parameter changes"):
        body = {
            "data": {"color": "black_and_white",
                     "size": "too big", "scale": "world"}
        }
    obj_id = new_object_id
    patch.patch_object(body, obj_id)
    patch.check_code_status_is_200()

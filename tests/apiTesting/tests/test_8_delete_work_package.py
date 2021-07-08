import time
from tests.apiTesting.api.project_api import ProjectApi
from tests.apiTesting.utils.utils import generate_random_name


def test_8_delete_work_package():

    new_work_package_name = generate_random_name()

    # Create Project
    response = ProjectApi().post_new_work_package(new_work_package_name)

    # Check Status Code 201 (CREATED)
    result_status = response.status_code
    assert result_status == 201, ("Result Status Code Is", result_status)

    # Get New Work Package Id
    response_json = response.json()
    new_work_package_id = response_json["id"]

    # Delete Project
    response = ProjectApi().delete_work_package(new_work_package_id)
    result_status = response.status_code

    # Check Status Code 204 (DELETED)
    assert result_status == 204, ("Result Status Code Is", result_status)

    # Check exist only after delete finished
    time.sleep(5)

    # Check If Project Exist
    response = ProjectApi().get_work_package_by_id(new_work_package_id)
    result_status = response.status_code

    # Check Status Code 404 (Not Found)
    assert result_status == 404, ("Result Status Code Is ", result_status)

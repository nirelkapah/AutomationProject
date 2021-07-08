import time
from tests.apiTesting.api.project_api import ProjectApi
from tests.apiTesting.utils.utils import generate_random_name


def test_4_delete_project():

    new_project_name = generate_random_name()

    # Create Project
    response = ProjectApi().post_new_project(new_project_name)

    # Check Status Code 201 (CREATED)
    result_status = response.status_code
    assert result_status == 201, ("Result Status Code Is", result_status)

    # Get New Project Id
    response_json = response.json()
    new_project_id = response_json["id"]

    # Delete Project
    response = ProjectApi().delete_project(new_project_id)
    result_status = response.status_code

    # Check Status Code 204 (DELETED)
    assert result_status == 204, ("Result Status Code Is", result_status)

    project_id = new_project_id

    # Check exist only after delete
    time.sleep(5)

    # Check If Project Exist
    response = ProjectApi().get_project_by_id(project_id)
    result_status = response.status_code

    # Check Status Code 404 (Not Found)
    assert result_status == 404, ("Result Status Code Is ", result_status)

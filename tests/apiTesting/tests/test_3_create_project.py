from tests.apiTesting.api.project_api import ProjectApi
from tests.apiTesting.utils.utils import generate_random_name


def test_3_create_project():

    new_project_name = generate_random_name()

    response = ProjectApi().post_new_project(new_project_name)

    result_status = response.status_code

    # Check Status Code 201 (CREATE)
    assert result_status == 201, ("Result Status Code Is", result_status)

    # Convert to JSON and get name
    response_json = response.json()
    actual_project_name = response_json["name"]
    expected_project_name = new_project_name

    # Check Project Name
    assert actual_project_name == expected_project_name, "Project Name Is Different Then Expected"

    # Convert to JSON and get name
    response_json = response.json()
    actual_project_identifier = response_json["identifier"]
    expected_project_identifier = new_project_name.replace(' ', '-')

    assert actual_project_identifier == expected_project_identifier, "Project Identifier Is Different Then Expected"



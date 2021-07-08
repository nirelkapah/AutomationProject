from tests.apiTesting.api.project_api import ProjectApi


def test_1_get_project():

    project_id = "3"
    project_name = "TestProject1"
    expected_project_description = "new description 6"

    response = ProjectApi().get_project_by_id(project_id)

    result_status = response.status_code

    # Check Status Code 200
    assert result_status == 200, ("Result Status Code Is", result_status)

    # Convert to JSON and get name
    response_json = response.json()
    actual_project_name = response_json["name"]
    expected_project_name = project_name

    # Check Project Name
    assert actual_project_name == expected_project_name, "Requested Project Name Is Different Then Expected"

    # Convert to JSON and get description
    response_json = response.json()
    actual_project = response_json["description"]
    actual_project_description = actual_project["raw"]
    assert actual_project_description == expected_project_description, "Requested Project Description Is Different Then Expected"




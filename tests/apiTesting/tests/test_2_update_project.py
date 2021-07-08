from tests.apiTesting.api.project_api import ProjectApi


def test_2_update_project():

    new_description = "new description 6"
    project_id = "3"

    response = ProjectApi().patch_project_description(project_id, new_description)
    result_status = response.status_code

    # Check Status Code 200
    assert result_status == 200, ("Result Status Code Is", result_status)

    response_json = response.json()
    description = response_json['description']
    actual_description = description['raw']
    expected_description = new_description

    assert actual_description == expected_description, "Response Returned different description then expected"





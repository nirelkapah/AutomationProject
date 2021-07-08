from tests.apiTesting.api.project_api import ProjectApi


def test_6_update_work_package():

    new_description = "new description 13"
    work_package_id = "34"

    # Get Lock Version for update
    response = ProjectApi().get_work_package_by_id(work_package_id)
    response_json = response.json()
    lock_version = response_json['lockVersion']

    response = ProjectApi().patch_work_package_description(work_package_id, new_description, lock_version)

    result_status = response.status_code
    # Check Status Code 200
    assert result_status == 200, ("Result Status Code Is", result_status)

    response_json = response.json()
    description = response_json['description']
    actual_description = description['raw']
    expected_description = new_description

    assert actual_description == expected_description, "Response Returned different description then expected"





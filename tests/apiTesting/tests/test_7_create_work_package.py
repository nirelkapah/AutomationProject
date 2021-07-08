from tests.apiTesting.api.project_api import ProjectApi
from tests.apiTesting.utils.utils import generate_random_name


def test_7_create_work_package():

    new_work_package_name = generate_random_name()

    response = ProjectApi().post_new_work_package(new_work_package_name)

    result_status = response.status_code
    # Check Status Code 201 (CREATE)
    assert result_status == 201, ("Result Status Code Is", result_status)

    # Convert to JSON and get name
    response_json = response.json()
    actual_work_package_name = response_json["subject"]
    expected_work_package_name = new_work_package_name

    # Check Work Space Name
    assert actual_work_package_name == expected_work_package_name, "Project Name Is Different Then Expected"


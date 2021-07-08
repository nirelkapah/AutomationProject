from tests.apiTesting.api.project_api import ProjectApi


def test_5_get_work_package():

    project_name = "TestProject1"
    task_name = "My Task 1"
    work_package_id = "34"

    response = ProjectApi().get_work_package_by_id(work_package_id)

    result_status = response.status_code
    # Check Status Code 200
    assert result_status == 200, ("Result Status Code Is", result_status)

    # Convert to JSON and get name
    response_json = response.json()
    actual_task_name = response_json["subject"]
    expected_task_name = task_name

    # Check Project Name
    assert actual_task_name == expected_task_name, "Requested Project Name Is Different Then Expected"

    # Convert to JSON and get task type
    response_json = response.json()
    actual_task = response_json["_links"]
    actual_task_type = actual_task["type"]
    actual_task_title = actual_task_type["title"]

    # Check Task Type
    assert actual_task_title == "Task", "Requested Project Type Is Different Then Expected"




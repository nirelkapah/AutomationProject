import json
from tests.apiTesting.api.rest_client import RestClient


class ProjectApi:

    def __init__(self):
        self.rest_client = RestClient

    # =================================PROJECT FUNCTIONS================================

    def get_project_by_id(self, project_id: str):
        response = self.rest_client().get(path=f"/api/v3/projects/{project_id}")
        return response

    def patch_project_description(self, project_id: str, new_description: str):

        payload = json.dumps({
            "description": {
                "raw": new_description
            }
        })

        response = self.rest_client().patch(path=f"/api/v3/projects/{project_id}", payload=payload)
        return response

    def post_new_project(self, new_project_name):

        payload = json.dumps({
            "name": new_project_name
        })

        response = self.rest_client().post(path="/api/v3/projects", payload=payload)
        return response

    def delete_project(self, project_id):

        response = self.rest_client().delete(path=f"/api/v3/projects/{project_id}")
        return response

    # ==================================WORK PACKAGES FUNCTIONS=================================

    # Get Work Package - /api/v3/work_packages/34
    def get_work_package_by_id(self, work_package_id: str):
        response = self.rest_client().get(path=f"/api/v3/work_packages/{work_package_id}")
        return response

    def patch_work_package_description(self, work_package_id: str, new_description: str, lock_version: int):

        payload = json.dumps({
            "lockVersion": lock_version,
            "_links": {},
            "description": {
                "raw": new_description
            }
        })

        response = self.rest_client().patch(path=f"/api/v3/work_packages/{work_package_id}", payload=payload)
        return response

    def post_new_work_package(self, new_work_package_name):

        payload = json.dumps({
            "subject": new_work_package_name,
            "_links": {
                "type": {
                    "href": "/api/v3/types/1",
                    "title": "Task"
                },
                "priority": {
                    "href": "/api/v3/priorities/8",
                    "title": "Normal"
                },
                "project": {
                    "href": "/api/v3/projects/3",
                    "title": "TestProject1"
                },
                "status": {
                    "href": "/api/v3/statuses/1",
                    "title": "New"
                }
            },
            "description": {
                "raw": "this is task"
            }
        })

        response = self.rest_client().post(path="/api/v3/work_packages", payload=payload)
        return response

    def delete_work_package(self, work_package_id):

        response = self.rest_client().delete(path=f"/api/v3/work_packages/{work_package_id}")
        return response

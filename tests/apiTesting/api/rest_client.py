import tests.apiTesting.env.config as config
import requests


class RestClient:

    __base_url = config.data.get("base_url")
    __headers = {
            'Authorization': 'Basic ' + config.data.get("token"),
            'Content-Type': 'application/json'
    }

    def get(self, path: str):

        response = requests.request("GET", url=self.__base_url + path, headers=self.__headers)
        return response

    def patch(self, path: str, payload):

        response = requests.request("PATCH", url=self.__base_url + path, headers=self.__headers, data=payload)
        return response

    def post(self, path: str, payload):

        response = requests.request("POST", url=self.__base_url + path, headers=self.__headers, data=payload)
        return response

    def delete(self, path: str):

        response = requests.request("DELETE", url=self.__base_url + path, headers=self.__headers)
        return response

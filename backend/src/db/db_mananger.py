from typing import Union
import requests
import json


class Db_manager:

    """
    A client class for interacting with a JSON server.

    Args:
        base_url (str): The base URL of the JSON server.

    Methods:
        get(resource: str) -> dict:
            Send a GET request to the JSON server to retrieve data from a specific resource.

        post(resource: str, data: dict) -> dict:
            Send a POST request to create a new resource on the JSON server.

        put(resource: str, data: dict) -> dict:
            Send a PUT request to update an existing resource on the JSON server.

        delete(resource: str) -> dict:
            Send a DELETE request to remove a resource from the JSON server.

    Example usage:

    >>> json_server = JSONServerClient("http://localhost:3000")
    >>> data = {"name": "John", "age": 30}
    >>> result = json_server.get("users")
    >>> created_user = json_server.post("users", data)
    >>> updated_user = json_server.put("users/1", {"age": 31})
    >>> deleted_user = json_server.delete("users/1")
    """

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url


    def create_table_in_db(
        self,
        path: str,
        table_name: str,
        default_value: Union[list, dict]=[]
    ) -> None:

        with open(path, "r") as json_file:
            existing_data = json.load(json_file)

        existing_data.setdefault(table_name, default_value)

        updated_data = existing_data.copy()

        json_file.close()

        with open(path, "w") as json_file:
            json.dump(updated_data, json_file)

    def get(self, resource: str) -> list:
        """
        Send a GET request to the JSON server to retrieve data from a specific resource.

        Args:
            resource (str): The name or path of the resource to retrieve.

        Returns:
            dict: The JSON response from the server.

        Raises:
            requests.exceptions.RequestException: If the GET request encounters an error.
        """

        url = f'{self.base_url}/{resource}'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def post(self, resource, data) -> dict:
        """
        Send a POST request to create a new resource on the JSON server.

        Args:
            resource (str): The name or path of the resource to create.
            data (dict): The data to include in the POST request's JSON body.

        Returns:
            dict: The JSON response from the server, typically confirming the creation.

        Raises:
            requests.exceptions.RequestException: If the POST request encounters an error.
        """
        url = f'{self.base_url}/{resource}'
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()


    def put(self, resource, data):
        """
        Send a PUT request to update an existing resource on the JSON server.

        Args:
            resource (str): The name or path of the resource to update.
            data (dict): The data to include in the PUT request's JSON body for the update.

        Returns:
            dict: The JSON response from the server, typically confirming the update.

        Raises:
            requests.exceptions.RequestException: If the PUT request encounters an error.
        """
        url = f"{self.base_url}/{resource}"
        response = requests.put(url, json=data)
        response.raise_for_status()
        return response.json()

    def delete(self, resource):
        """
        Send a DELETE request to remove a resource from the JSON server.

        Args:
            resource (str): The name or path of the resource to delete.

        Returns:
            dict: The JSON response from the server, typically confirming the deletion.

        Raises:
            requests.exceptions.RequestException: If the DELETE request encounters an error.
        """
        
        url = f"{self.base_url}/{resource}"
        response = requests.delete(url)
        response.raise_for_status()
        return response.json()

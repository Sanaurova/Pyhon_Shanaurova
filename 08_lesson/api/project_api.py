from requests import Response
from api.client import YougileClient


class ProjectAPI:

    def __init__(self, client: YougileClient):
        self.client = client

    def create_project(self, title: str) -> Response:
        """
        Создание нового проекта.
        POST /api-v2/projects
        Документация:
        https://ru.yougile.com/api-v2#/operations/ProjectController_create
        """
        payload = {"title": title}
        response = self.client._request("POST", "projects", json=payload)
        return response

    def get_project(self, project_id: str) -> Response:
        response = self.client._request("GET", f"projects/{project_id}")
        return response

    def update_project(self, project_id: str, title: str) -> Response:
        payload = {"title": title}
        response = self.client._request(
            "PUT", f"projects/{project_id}", json=payload
        )
        return response

    def delete_project(self, project_id: str) -> Response:
        response = self.client._request("DELETE", f"projects/{project_id}")
        return response

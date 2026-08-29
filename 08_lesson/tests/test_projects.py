import pytest
from api.client import YougileClient
from api.project_api import ProjectAPI


@pytest.fixture
def project_api(api_key, base_url):
    client = YougileClient(base_url, api_key)
    return ProjectAPI(client)


@pytest.fixture
def created_project_id(project_api):
    """Создаёт проект для тестов и удаляет после выполнения."""
    response = project_api.create_project(
        "Тестовый проект для API-тестов"
    )
    assert response.status_code == 201, (
        f"Не удалось создать проект: {response.text}"
    )
    project_id = response.json().get("id")
    yield project_id
    project_api.delete_project(project_id)


class TestProjectPositive:
    def test_create_project_success(self, project_api):
        project_title = "Новый проект"
        response = project_api.create_project(project_title)
        assert response.status_code == 201
        data = response.json()
        assert "id" in data
        # Проверяем, что проект создан с правильным названием
        get_resp = project_api.get_project(data["id"])
        assert get_resp.status_code == 200
        assert get_resp.json().get("title") == project_title

    def test_get_project_success(self, project_api, created_project_id):
        response = project_api.get_project(created_project_id)
        assert response.status_code == 200
        data = response.json()
        assert data.get("id") == created_project_id
        assert "title" in data

    def test_update_project_success(self, project_api, created_project_id):
        new_title = "Обновлённое название проекта"
        response = project_api.update_project(created_project_id, new_title)
        assert response.status_code == 200
        # Проверяем через GET, что название изменилось
        get_resp = project_api.get_project(created_project_id)
        assert get_resp.status_code == 200
        data = get_resp.json()
        assert data.get("title") == new_title, (
            f"Ожидалось '{new_title}', получено '{data.get('title')}'"
        )


class TestProjectNegative:
    def test_create_project_without_title(self, project_api):
        response = project_api.create_project("")
        assert response.status_code == 400
        error_data = response.json()
        assert "error" in error_data or "message" in error_data

    def test_get_nonexistent_project(self, project_api):
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = project_api.get_project(fake_id)
        assert response.status_code == 404
        error_data = response.json()
        assert "error" in error_data or "message" in error_data

    def test_update_nonexistent_project(self, project_api):
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = project_api.update_project(
            fake_id, "Новое название"
        )
        assert response.status_code == 404
        error_data = response.json()
        assert "error" in error_data or "message" in error_data

    def test_update_project_with_empty_title(
            self, project_api, created_project_id
    ):
        response = project_api.update_project(created_project_id, "")
        assert response.status_code == 400
        error_data = response.json()
        assert "error" in error_data or "message" in error_data

    def test_create_project_with_invalid_auth(self, base_url):
        invalid_client = YougileClient(
            base_url, "invalid_token_12345"
        )
        invalid_api = ProjectAPI(invalid_client)
        response = invalid_api.create_project(
            "Проект с невалидным токеном"
        )
        assert response.status_code == 401

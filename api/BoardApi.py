import requests
import allure
from faker import Faker


fake = Faker()


class BoardApi:
    """API-клиент для работы с досками YouGile."""
    def __init__(self, config: dict) -> None:
        self.__url = config['base_url_api']
        self.project_id = config['project_id']
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {config['token']}"
        }

    @staticmethod
    def random_board_name() -> str:
        """Сгенерировать случайное имя доски."""
        return f"Пробная доска: {fake.catch_phrase()}"

    @allure.story("Boards API")
    @allure.step("Получить список всех досок")
    def get_all_boards(self) -> dict:
        """GET /boards — получить список всех досок."""
        url = self.__url + "/boards"

        response = requests.request("GET", url, headers=self.headers)
        return response.json()

    @allure.story("Boards API")
    @allure.step("Создать доску")
    def create_board(self, name: str) -> dict:
        """POST /boards — создать новую доску."""
        url = self.__url + "/boards"
        payload = {
            'title': name,
            'projectId': self.project_id,
            'stickers': {
                'timer': False,
                'deadline': True,
                'stopwatch': True,
                'timeTracking': True,
                'assignee': True,
                'repeat': True
                }
            }
        response = requests.request("POST", url,
                                    json=payload, headers=self.headers)
        return response.json()

    @allure.story("Boards API")
    @allure.step("Получить доску по ID")
    def find_board(self, id_board: str) -> dict:
        """GET /boards/{id} — получить доску по ID."""
        url = self.__url + "/boards/" + id_board
        response = requests.request("GET", url, headers=self.headers)
        return response.json()

    @allure.story("Boards API")
    @allure.step("Изменить название доски по id")
    def update_board(self, id_board: str, name: str) -> dict:
        """PUT /boards/{id} — изменить название доски."""
        url = self.__url + "/boards/" + id_board
        payload = {
            'title': name,
            'projectId': self.project_id,
            'stickers': {
                'deadline': True,
                'assignee': True
                }
            }
        response = requests.request("PUT", url,
                                    json=payload, headers=self.headers)

        return response.json()

    @allure.story("Boards API")
    @allure.step("Удалить доску по ID: {id_board}")
    def delete_board(self, id_board: str) -> dict:
        """PUT /boards/{id} с deleted=true — удалить доску."""
        url = self.__url + "/boards/" + id_board

        payload = {
            'deleted': True,
            }
        response = requests.request("PUT", url,
                                    json=payload, headers=self.headers)
        return response.json()

import allure
import pytest
import os
from pathlib import Path
from dotenv import load_dotenv
from selenium.webdriver.ie.webdriver import WebDriver

from pages.MainPage import MainPage
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from pages.AuthPage import AuthPage
from api.BoardApi import BoardApi

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)


@pytest.fixture(scope="session")
def config() -> dict:
    return {
        "base_url_api": os.getenv("BASE_URL_API"),
        "base_url_ui": os.getenv("BASE_URL_UI"),
        "password": os.getenv("PASSWORD"),
        "email": os.getenv("EMAIL"),
        "token": os.getenv("API_TOKEN"),
        "project_id": os.getenv("PROJECT_ID"),
        "timeout": int(os.getenv("TIMEOUT", 10)),
        "browser_name": os.getenv("BROWSER_NAME", "chrome")
    }


@pytest.fixture()
def browser(config):
    """Открыть и настроить браузер, закрыть после теста."""
    with allure.step("Открыть и настроить браузер"):
        browser_name = config['browser_name'].lower()
        if browser_name == "chrome":
            browser = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()))
        else:
            browser = webdriver.Firefox(
                service=Service(GeckoDriverManager().install()))

        browser.implicitly_wait(config['timeout'])
        browser.maximize_window()
    yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture()
def auth(browser: WebDriver, config: dict) -> AuthPage:
    """Авторизоваться и вернуть AuthPage."""
    with allure.step("Авторизоваться"):
        auth_page = AuthPage(browser, config)
        auth_page.go()
        auth_page.login_as(config['email'], config['password'])
        return auth_page


@pytest.fixture
def board(config: dict) :
    """Создать доску до теста и удалить её после."""
    api = BoardApi(config)

    with allure.step("Создать рандомное имя доски "):
        name = api.random_board_name()
    with allure.step(f"Создать доску с именем {name}"):
        resp = api.create_board(name)
        id_board = resp['id']
    yield id_board, name
    with allure.step(f"Удалить созданную доску {name}"):
        api.delete_board(id_board)


@pytest.fixture()
def api(config: dict) -> BoardApi:
    """API-клиент, настроенный по config."""
    return BoardApi(config)


@pytest.fixture()
def main_page(browser: WebDriver, config: dict, auth: AuthPage) -> MainPage:
    """MainPage, доступная только после авторизации."""
    return MainPage(browser, config)

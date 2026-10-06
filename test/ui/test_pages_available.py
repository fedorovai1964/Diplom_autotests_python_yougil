import allure
import pytest

pytestmark = [pytest.mark.ui]


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Navigation UI")
@allure.title("Успешный переход на страницу My Tasks")
def test_pages_available_tasks(browser, config, auth, main_page) -> None:
    with allure.step("Открыть страницу My Tasks"):
        main_page.get_tasks()

    current_url = main_page.get_current_url()
    with allure.step(f"Проверить, что URL {current_url}"
                     f" оканчивается на /my-tasks"):
        assert current_url.endswith("my-tasks")


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Navigation UI")
@allure.title("Успешный переход на страницу My Company")
def test_pages_available_projects(browser, auth, main_page) -> None:
    with allure.step("Открыть страницу My Company"):
        main_page.get_company()

    current_url = main_page.get_current_url()
    with allure.step(f"Проверить, что URL {current_url}"
                     f" оканчивается на /projects"):
        assert current_url.endswith("projects")


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Navigation UI")
@allure.title("Успешный переход на страницу профиля пользователя")
def test_pages_available_profile(browser, auth, main_page) -> None:
    with allure.step("Открыть меню учётной записи"):
        main_page.open_menu()

    current_url = main_page.get_current_url()
    with allure.step(f"Проверить, что URL {current_url}"
                     f" оканчивается на /account"):
        assert current_url.endswith("account")

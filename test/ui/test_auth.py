import allure
import pytest

pytestmark = [pytest.mark.ui]

@allure.story("Auth UI")
@allure.title("Успешная авторизация в YouGile по email и паролю")
def test_auth_(auth):
    with allure.step("Проверить, что на главной есть 'My company'"):
        assert auth.company_search() == "My company"
    with allure.step("Проверить, что пользователь авторизован"):
        assert auth.is_logged_in()


@allure.story("Auth UI")
@allure.title("Email в профиле совпадает с введённым при авторизации")
def test_auth_email(browser, config, auth, main_page):
    main_page.open_menu()

    with allure.step(f"Проверить, что email в профиле = {config['email']}"):
        info = main_page.get_account_info()
        assert info == config['email']

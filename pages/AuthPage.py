import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage():
    """Страница авторизации YouGile."""
    def __init__(self, driver: WebDriver, config: dict) -> None:
        self.__url = config['base_url_ui']
        self.__driver = driver
        self.timeout = config['timeout']
        self.wait = WebDriverWait(self.__driver, self.timeout)
        self.locators = {
            "email": "[placeholder='example@mail.ru']",
            "password": "[autocomplete='current-password']",
            "sign_in": "div[role='button']",
            "main_page": "//div[@class='text-sm-semibold"
                         " text-panel-text-primary cursor-default']",
            "user_avatar": "[data-testid='profile-avatar-item']",
        }

    @allure.step("Перейти на страницу авторизации")
    def go(self) -> "AuthPage":
        self.__driver.get(self.__url)
        return self

    def login_as(self, email: str, password: str) -> "AuthPage":
        with allure.step("Авторизоваться как {email}"):
            self.wait.until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR, self.locators["email"]),))
            email_field = self.__driver.find_element(
                By.CSS_SELECTOR, self.locators["email"])
            email_field.clear()
            email_field.send_keys(email)

            password_field = self.__driver.find_element(
                By.CSS_SELECTOR, self.locators["password"])
            password_field.clear()
            password_field.send_keys(password)

            self.__driver.find_element(
                By.CSS_SELECTOR, self.locators['sign_in']).click()

            self.wait.until(
                EC.visibility_of_element_located((
                    By.XPATH, self.locators["main_page"])))
            return self


    @allure.step("Получить заголовок компании на главной странице")
    def company_search(self) -> str:
        search_title = self.__driver.find_element(
            By.XPATH, self.locators["main_page"]).text
        return search_title

    @allure.step("Проверить, что пользователь авторизован")
    def is_logged_in(self) -> bool:
        try:
            self.wait.until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR, self.locators['user_avatar']))
            )
            return True
        except Exception:
            return False

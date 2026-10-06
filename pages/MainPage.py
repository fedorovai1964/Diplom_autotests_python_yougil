import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver: WebDriver, config: dict) -> None:
        self.__driver = driver
        self.timeout = config['timeout']
        self.wait = WebDriverWait(self.__driver, self.timeout)
        self.locators = {
            "open_menu": "//div[@class='truncate ml-6 text-14 leading-4']",
            "avatar": "[class='user-avatar']",
            "email": "[placeholder='Displayed name…']",
            "my_tasks": "//div[normalize-space()='My Tasks']",
            "my_company": "//div[normalize-space()='My company']",
            "user_avatar": "[data-testid='profile-avatar-item']",
        }

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.__driver.current_url

    @allure.step("Открыть меню учетной записи")
    def open_menu(self) -> "MainPage":
        self.__driver.find_element(
            By.XPATH, self.locators['open_menu']).click()
        return self

    @allure.step("Получить email из меню учётной записи")
    def get_account_info(self) -> str:

        (self.wait.until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, self.locators['avatar']))
        ))

        search_email = self.__driver.find_element(
            By.CSS_SELECTOR, self.locators['email'])
        search_value = search_email.get_attribute('value')

        return search_value

    @allure.step("Открыть страницу My tasks")
    def get_tasks(self) -> "MainPage":
        self.__driver.find_element(
            By.XPATH, self.locators['my_tasks']).click()
        return self

    @allure.step("Открыть страницу My company")
    def get_company(self) -> "MainPage":
        self.__driver.find_element(
            By.XPATH, self.locators['my_company']).click()
        return self

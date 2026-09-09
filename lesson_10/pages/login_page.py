from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object для страницы авторизации Saucedemo."""

    # Локаторы
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self) -> "LoginPage":
        """
        Открыть страницу авторизации.
        :return: экземпляр текущей страницы
        """
        self.driver.get("https://www.saucedemo.com/")
        return self

    def login(self, username: str, password: str) -> "LoginPage":
        """
        Выполнить вход в систему.
        :param username: логин пользователя
        :param password: пароль пользователя
        :return: экземпляр текущей страницы
        """
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def get_error_text(self) -> str:
        """
        Получить текст сообщения об ошибке.
        :return: текст ошибки
        """
        return self.get_text(self.ERROR_MESSAGE)

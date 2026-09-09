from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Базовый класс для всех Page Object'ов.
    Содержит общие методы для работы с элементами.
    """

    def __init__(self, driver, timeout: int = 120):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator):
        """
        Клик по элементу с ожиданием его кликабельности.
        :param locator: кортеж (By, значение) – локатор элемента
        :return: экземпляр текущей страницы (для цепочки вызовов)
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return self

    def fill(self, locator, text):
        """
        Заполнение поля ввода, предварительно очищая его.
        :param locator: кортеж (By, значение) – локатор элемента
        :param text: текст для ввода
        :return: экземпляр текущей страницы
        """
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        return self

    def get_text(self, locator):
        """
        Получение текста элемента.
        :param locator: кортеж (By, значение) – локатор элемента
        :return: текст элемента
        """
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.text

    def is_displayed(self, locator):
        """
        Проверка видимости элемента.
        :param locator: кортеж (By, значение) – локатор элемента
        :return: True, если элемент видим, иначе False
        """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except Exception:
            return False

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CalculatorPage(BasePage):
    # Локаторы
    DELAY_INPUT = (By.ID, "delay")
    SCREEN_RESULT = (By.CLASS_NAME, "screen")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")

    def open(self) -> "CalculatorPage":
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        return self

    def set_delay(self, delay: str) -> "CalculatorPage":
        """
        Установить задержку в поле #delay.
        :param delay: строка с числом секунд (например, "45")
        :return: Экземпляр текущей страницы
        """
        self.fill(self.DELAY_INPUT, delay)
        return self

    def click_seven(self) -> "CalculatorPage":
        """Нажать кнопку '7'."""
        self.click(self.BUTTON_7)
        return self

    def click_eight(self) -> "CalculatorPage":
        """Нажать кнопку '8'."""
        self.click(self.BUTTON_8)
        return self

    def click_plus(self) -> "CalculatorPage":
        """Нажать кнопку '+'."""
        self.click(self.BUTTON_PLUS)
        return self

    def click_equals(self) -> "CalculatorPage":
        """Нажать кнопку '='."""
        self.click(self.BUTTON_EQUALS)
        return self

    def get_result_text(self) -> str:
        """
        Получить текст результата из поля вывода.
        :return: Текст на экране калькулятора
        """
        return self.get_text(self.SCREEN_RESULT)

    def wait_for_result(self, expected: str) -> "CalculatorPage":
        """
        Ожидать появления заданного значения на экране.
        :param expected: Ожидаемый текст (например, "15")
        :return: Экземпляр текущей страницы
        """

        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN_RESULT, expected)
        )
        return self

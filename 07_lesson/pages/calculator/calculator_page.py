from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    # Локаторы элементов
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN_RESULT = (By.CSS_SELECTOR, ".screen")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 120)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, delay: str):
        delay_field = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT)
        )
        delay_field.clear()
        delay_field.send_keys(delay)

    def click_seven(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_7)).click()

    def click_eight(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_8)).click()

    def click_plus(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_PLUS)).click()

    def click_equals(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_EQUALS)).click()

    def get_result_text(self) -> str:
        return self.driver.find_element(*self.SCREEN_RESULT).text

    def wait_for_result(self, expected: str):
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN_RESULT, expected)
        )

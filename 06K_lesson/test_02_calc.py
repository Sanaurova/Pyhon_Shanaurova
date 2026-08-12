import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--page-load-timeout=300")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(180)
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    # Тест калькулятора с задержкой 45 секунд.
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )
    wait = WebDriverWait(driver, 60)

    # Ввод задержки
    delay_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
    )
    delay_input.clear()
    delay_input.send_keys("45")

    # Кнопки: 7, +, 8, =
    button_7 = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='7']")
        )
    )
    button_7.click()

    button_plus = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='+']")
        )
    )
    button_plus.click()

    button_8 = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='8']")
        )
    )
    button_8.click()

    button_equals = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='=']")
        )
    )
    button_equals.click()

    # Ожидание результата "15" на экране
    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".screen"), "15"
        )
    )

    result_text = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result_text == "15", f"Ожидалось '15', получено '{result_text}'"

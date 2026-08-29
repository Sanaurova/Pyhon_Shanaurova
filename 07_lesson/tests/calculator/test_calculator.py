import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator.calculator_page import CalculatorPage


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
    # Создаём объект страницы
    calc_page = CalculatorPage(driver)

    # Шаги теста
    calc_page.open()
    calc_page.set_delay("45")
    calc_page.click_seven()
    calc_page.click_plus()
    calc_page.click_eight()
    calc_page.click_equals()

    # Ожидание появления результата
    calc_page.wait_for_result("15")

    # Проверка (assert) – только здесь!
    result = calc_page.get_result_text()
    assert result == "15", f"Ожидалось '15', получено '{result}'"

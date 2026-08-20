import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="function")
def driver():
    options = EdgeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--page-load-timeout=180")

    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=options)
    yield driver
    driver.quit()


def test_form_validation(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )
    wait = WebDriverWait(driver, 10)

    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "job-position": "QA",
        "company": "SkyPro",
    }

    for name, value in form_data.items():
        field = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, f"input[name='{name}']")
            )
        )
        field.clear()
        if value:
            field.send_keys(value)

    submit = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and text()='Submit']")
        )
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit)
    driver.execute_script("arguments[0].click();", submit)

    # Проверка: Zip code – красный
    zip_element = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#zip-code.alert-danger")
        )
    )
    assert "alert-danger" in zip_element.get_attribute("class"), \
        "Zip code не подсвечен красным"

    # Проверка: остальные поля – зелёные
    green_field_ids = [
        "first-name", "last-name", "address",
        "city", "country", "e-mail", "phone",
        "job-position", "company"
    ]

    for field_id in green_field_ids:
        field = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, f"#{field_id}.alert-success")
            )
        )
        is_field_green = "alert-success" in field.get_attribute("class")
        assert is_field_green, f"Поле {field_id} не подсвечено зелёным"

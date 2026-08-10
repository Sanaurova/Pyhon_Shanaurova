import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    chrome_driver_path = os.path.join(current_dir, "chromedriver.exe")

    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--page-load-timeout=60")

    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(60)

    driver.get("https://httpbin.qa-territory.online/forms/post")
    print(f"Начальный URL: {driver.current_url}")

    # Поле ввода имени
    name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "custname"))
    )
    name_field.clear()
    name_field.send_keys("Марина")
    print("Имя введено")

    # Кнопка Submit — исправленный локатор
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Submit order']")
        )
    )
    print("Кнопка найдена")

    driver.execute_script("arguments[0].click();", submit_button)
    print("Кнопка нажата")

    # Проверка изменения URL
    try:
        WebDriverWait(driver, 15).until(
            EC.url_changes("https://httpbin.qa-territory.online/forms/post")
        )
        new_url = driver.current_url
        print(f"URL после отправки: {new_url}")
        assert new_url != "https://httpbin.qa-territory.online/forms/post", (
            "URL не изменился"
        )
    except Exception:
        print(f"Текущий URL: {driver.current_url}")
        raise

    driver.quit()

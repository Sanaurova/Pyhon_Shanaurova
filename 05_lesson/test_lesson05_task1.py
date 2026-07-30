import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_navigation():
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

    driver.get("https://httpbin.qa-territory.online")
    print(f"1. Начальный URL: {driver.current_url}")

    # Находим ссылку
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "HTML Form"))
    )
    # Выводим атрибут href
    href = link.get_attribute("href")
    print(f"2. Атрибут href ссылки: {href}")

    # Кликаем через JavaScript
    driver.execute_script("arguments[0].click();", link)
    print(f"3. URL сразу после клика: {driver.current_url}")

    # Ждём изменения URL (но не конкретного, а любого)
    try:
        WebDriverWait(driver, 10).until(
            EC.url_changes("https://httpbin.qa-territory.online")
        )
        print(f"4. URL после изменения: {driver.current_url}")
    except Exception:
        print("4. URL не изменился за 10 секунд")

    # Проверка, что URL содержит "/forms/post"
    assert "/forms/post" in driver.current_url, (
        f"Ожидался URL с '/forms/post', получен: {driver.current_url}"
    )

    driver.back()
    WebDriverWait(driver, 10).until(
        EC.url_contains("httpbin.qa-territory.online")
    )
    assert (
        driver.current_url.rstrip('/') == "https://httpbin.qa-territory.online"
    )

    driver.quit()

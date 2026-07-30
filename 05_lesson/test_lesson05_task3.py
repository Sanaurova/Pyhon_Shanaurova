import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_multiple_elements():
    # Путь к chromedriver.exe в папке 05_lesson
    current_dir = os.path.dirname(os.path.abspath(__file__))
    chrome_driver_path = os.path.join(current_dir, "chromedriver.exe")

    # Настройки для стабильной работы
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

    # 1. Открыть страницу
    driver.get("https://httpbin.qa-territory.online/links/10")
    print(f"Страница загружена: {driver.current_url}")

    # 2. Найти все ссылки (тег <a>)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "a"))
    )
    links = driver.find_elements(By.TAG_NAME, "a")
    print(f"Найдено ссылок: {len(links)}")

    # 3. Проверить, что количество ссылок равно 9
    assert len(links) == 9, f"Ожидалось 9 ссылок, найдено {len(links)}"

    # 4. Проверить, что все ссылки отображаются на странице
    for i, link in enumerate(links):
        assert link.is_displayed(), f"Ссылка с индексом {i} не отображается"

    # 5. Проверить, что текст первой ссылки содержит "1"
    first_link_text = links[0].text
    print(f"Текст первой ссылки: '{first_link_text}'")
    assert "1" in first_link_text, (
        f"Первая ссылка не содержит '1', текст: '{first_link_text}'"
    )

    print("Все проверки пройдены успешно!")
    driver.quit()

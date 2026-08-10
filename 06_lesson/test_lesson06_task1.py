from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_dynamic_loading():
    # Настройки для стабильной работы
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--page-load-timeout=60")

    # Автоматическое управление драйвером через webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(60)

    # 1. Открыть страницу
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Найти и нажать кнопку "Start"
    start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_button.click()

    # 3. Дождаться появления текста "Hello World!"
    hello_text_element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "finish"))
    )

    # 4. Сделать скриншот
    driver.save_screenshot("dynamic_loading_screenshot.png")
    print("Скриншот сохранён как dynamic_loading_screenshot.png")

    # 5. Проверить текст
    actual_text = hello_text_element.text
    assert actual_text == "Hello World!", f"Ожидался 'Hello World!', получен '{actual_text}'"

    print("Тест пройден успешно!")
    driver.quit()
    
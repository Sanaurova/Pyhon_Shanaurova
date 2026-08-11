from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_session_storage_auth():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--page-load-timeout=120")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/151.0.7922.76 Safari/537.36"
    )
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(120)

    # 1. Открыть главную страницу
    driver.get("https://gitflic.ru/")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # 2. Установить куки пользователя 1 (только через add_cookie)
    cookies_user1 = [
        {
            "name": "SESSION",
            "value": "NTU5OWVjZWUtODk2OS00ZWU4LTk5ZGUtZjJhYzlhMjc1ZDUx",
            "domain": ".gitflic.ru",
            "path": "/"
        },
        {
            "name": "X-CSRF-TOKEN",
            "value": "09a354b9-4b82-488a-8e92-9b028071ccb2",
            "domain": ".gitflic.ru",
            "path": "/"
        },
    ]
    for cookie in cookies_user1:
        driver.add_cookie(cookie)

    # Обновить страницу и дождаться загрузки
    driver.refresh()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # 3. Переход на профиль пользователя 1
    driver.get("https://gitflic.ru/user/marina1")
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".user-profile__username")
        )
    )
    url_user1 = driver.current_url

    # 4. Разлогиниться (очистка кук)
    driver.delete_all_cookies()

    # 5. Установить куки пользователя 2
    cookies_user2 = [
        {
            "name": "SESSION",
            "value": "NDZlMTU2NWItNmM2NS00NGNkLWFmOTktNWJmN2RjYTNmMzJh",
            "domain": ".gitflic.ru",
            "path": "/"
        },
        {
            "name": "X-CSRF-TOKEN",
            "value": "f773b613-5a90-4650-8330-23602de6ae3c",
            "domain": ".gitflic.ru",
            "path": "/"
        },
    ]
    for cookie in cookies_user2:
        driver.add_cookie(cookie)

    driver.refresh()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # 6. Переход на профиль пользователя 2
    driver.get("https://gitflic.ru/user/marina2")
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".user-profile__name")
        )
    )
    url_user2 = driver.current_url

    # 7. Сравнение URL
    assert url_user1 != url_user2, f"URL совпадают: {url_user1}"

    driver.quit()

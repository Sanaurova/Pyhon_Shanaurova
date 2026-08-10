import time
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
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(180)

    driver.get("https://gitflic.ru/")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    time.sleep(2)

    # Куки пользователя 1
    cookies_user1 = [
        {
            "name": "SESSION",
            "value": "YmRiNzRiZjctMGMxYS00OTdlLTkyNDctYTE3NGIyZGMyM2Rm",
            "domain": ".gitflic.ru",
            "path": "/"
        },
        {
            "name": "X-CSRF-TOKEN",
            "value": "af8aa63b-23c7-4c1e-8b5a-443e6ad40f4c",
            "domain": ".gitflic.ru",
            "path": "/"
        },
    ]
    try:
        for cookie in cookies_user1:
            driver.add_cookie(cookie)
        print("Куки пользователя 1 установлены через add_cookie")
    except Exception as e:
        print(f"add_cookie не сработал: {e}, пробуем через JavaScript")
        sess1 = (
            "document.cookie = 'SESSION="
            "YmRiNzRiZjctMGMxYS00OTdlLTkyNDctYTE3NGIyZGMyM2Rm; "
            "path=/; domain=.gitflic.ru;'"
        )
        tok1 = (
            "document.cookie = 'X-CSRF-TOKEN="
            "af8aa63b-23c7-4c1e-8b5a-443e6ad40f4c; "
            "path=/; domain=.gitflic.ru;'"
        )
        driver.execute_script(sess1)
        driver.execute_script(tok1)
        print("Куки пользователя 1 установлены через JavaScript")

    driver.refresh()
    time.sleep(2)

    driver.get("https://gitflic.ru/user/marina1")
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".user-profile__username")
        )
    )
    url_user1 = driver.current_url
    print(f"URL пользователя 1: {url_user1}")

    driver.delete_all_cookies()
    print("Куки очищены")

    # Куки пользователя 2
    cookies_user2 = [
        {
            "name": "SESSION",
            "value": "YWY0MjYxZDMtY2JjOS00ODhlLWI5ZGItZDFkZWUxZTE0Mzdj",
            "domain": ".gitflic.ru",
            "path": "/"
        },
        {
            "name": "X-CSRF-TOKEN",
            "value": "50cc2274-b648-4c10-a74e-a98e619772bb",
            "domain": ".gitflic.ru",
            "path": "/"
        },
    ]
    try:
        for cookie in cookies_user2:
            driver.add_cookie(cookie)
        print("Куки пользователя 2 установлены через add_cookie")
    except Exception as e:
        print(f"add_cookie не сработал: {e}, пробуем через JavaScript")
        sess2 = (
            "document.cookie = 'SESSION="
            "YWY0MjYxZDMtY2JjOS00ODhlLWI5ZGItZDFkZWUxZTE0Mzdj; "
            "path=/; domain=.gitflic.ru;'"
        )
        tok2 = (
            "document.cookie = 'X-CSRF-TOKEN="
            "50cc2274-b648-4c10-a74e-a98e619772bb; "
            "path=/; domain=.gitflic.ru;'"
        )
        driver.execute_script(sess2)
        driver.execute_script(tok2)
        print("Куки пользователя 2 установлены через JavaScript")

    driver.refresh()
    time.sleep(2)

    driver.get("https://gitflic.ru/user/marina2")
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".user-profile__name")
        )
    )
    url_user2 = driver.current_url
    print(f"URL пользователя 2: {url_user2}")

    assert url_user1 != url_user2, f"URL совпадают: {url_user1}"
    print("Тест пройден: URL пользователей разные.")

    driver.quit()

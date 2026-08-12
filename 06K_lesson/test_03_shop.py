import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def driver():
    options = FirefoxOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    driver.set_page_load_timeout(300)
    yield driver
    driver.quit()


def test_shop_checkout_total(driver):
    wait = WebDriverWait(driver, 10)

    # 1. Открыть сайт и авторизоваться
    driver.get("https://www.saucedemo.com/")
    username = wait.until(EC.presence_of_element_located(
        (By.ID, "user-name")
        )
    )
    username.send_keys("standard_user")
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # 2. Добавить товары в корзину
    backpack_selector = (
        "[data-test='add-to-cart-sauce-labs-backpack']"
    )
    add_backpack = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, backpack_selector))
    )
    add_backpack.click()

    tshirt_selector = (
        "[data-test='add-to-cart-"
        "sauce-labs-bolt-t-shirt']"
    )
    add_tshirt = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, tshirt_selector))
    )
    add_tshirt.click()

    onesie_selector = (
        "[data-test='add-to-cart-"
        "sauce-labs-onesie']"
    )
    add_onesie = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, onesie_selector))
    )
    add_onesie.click()

    # 3. Перейти в корзину
    cart_icon = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
        )
    )
    cart_icon.click()

    # 4. Нажать Checkout
    checkout_btn = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test='checkout']")
        )
    )
    checkout_btn.click()

    # 5. Заполнить форму
    first_name = wait.until(EC.presence_of_element_located(
        (By.ID, "first-name")
        )
    )
    first_name.send_keys("Валентина")
    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Иванова")
    postal_code = driver.find_element(By.ID, "postal-code")
    postal_code.send_keys("665714")

    # 6. Нажать Continue
    continue_btn = driver.find_element(
        By.CSS_SELECTOR, "[data-test='continue']"
    )
    continue_btn.click()

    # 7. Прочитать итоговую стоимость
    total_label = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[data-test='total-label']")
        )
    )
    total_text = total_label.text
    total_value = total_text.replace("Total: ", "").strip()

    # 8. Проверка
    assert total_value == "$58.29", (
        f"Ожидалась $58.29, получено '{total_value}'"
    )

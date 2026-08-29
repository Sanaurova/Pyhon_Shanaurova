from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class InventoryPage:
    # Локаторы для кнопок добавления конкретных товаров
    BACKPACK_ADD = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_TSHIRT_ADD = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_ADD = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack(self):
        self.wait.until(EC.element_to_be_clickable(
            self.BACKPACK_ADD
        )).click()

    def add_bolt_tshirt(self):
        self.driver.find_element(*self.BOLT_TSHIRT_ADD).click()

    def add_onesie(self):
        self.driver.find_element(*self.ONESIE_ADD).click()

    def get_cart_count(self) -> int:
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            return int(badge.text)
        except (NoSuchElementException, ValueError):
            return 0

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()

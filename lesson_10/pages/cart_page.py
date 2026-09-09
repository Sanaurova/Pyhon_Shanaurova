from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page Object для страницы корзины."""

    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def proceed_to_checkout(self) -> "CartPage":
        """Нажать кнопку 'Checkout' для перехода к оформлению заказа."""
        self.click(self.CHECKOUT_BUTTON)
        return self

    def get_cart_items_count(self) -> int:
        """
        Получить количество товаров в корзине.
        :return: количество элементов с классом cart_item
        """
        return len(self.driver.find_elements(*self.CART_ITEMS))

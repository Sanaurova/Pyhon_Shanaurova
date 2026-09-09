import re
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page Object для главной страницы магазина (каталог товаров)."""

    # Локаторы для кнопок добавления в корзину
    BACKPACK_ADD = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_TSHIRT_ADD = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_ADD = (By.ID, "add-to-cart-sauce-labs-onesie")
    # Корзина
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack(self) -> "InventoryPage":
        """Добавить товар 'Sauce Labs Backpack' в корзину."""
        self.click(self.BACKPACK_ADD)
        return self

    def add_bolt_tshirt(self) -> "InventoryPage":
        """Добавить товар 'Sauce Labs Bolt T-Shirt' в корзину."""
        self.click(self.BOLT_TSHIRT_ADD)
        return self

    def add_onesie(self) -> "InventoryPage":
        """Добавить товар 'Sauce Labs Onesie' в корзину."""
        self.click(self.ONESIE_ADD)
        return self

    def get_cart_count(self) -> int:
        """
        Получить количество товаров в корзине (значок).
        :return: число товаров или 0, если значок отсутствует
        """
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            return int(badge.text)
        except Exception:
            return 0

    def go_to_cart(self) -> "InventoryPage":
        """Перейти в корзину."""
        self.click(self.CART_LINK)
        return self

    def get_item_price(self, item_name: str) -> float:
        """
        Получить цену товара по его названию.
        :param item_name: название товара
        :return: цена в виде числа (float)
        """

        price_locator = (
            By.XPATH,
            f"//div[text()='{item_name}']/ancestor::"
            f"div[@class='inventory_item']//div[@class='inventory_item_price']"
        )

        price_text = self.get_text(price_locator)
        if not price_text:
            raise ValueError(
                f"Цена для товара '{item_name}' не найдена на странице"
            )

        # Удаляем все символы, кроме цифр, точки и запятой
        cleaned = re.sub(r'[^\d.,]', '', price_text)

        # Если после очистки ничего не осталось – ошибка
        if not cleaned:
            raise ValueError(
                f"Не удалось извлечь число из строки: '{price_text}'"
            )

        # Заменяем запятую на точку
        cleaned = cleaned.replace(',', '.')

        # Проверяем, что число корректное
        try:
            return float(cleaned)
        except ValueError as e:
            raise ValueError(
                f"Некорректный формат числа: '{cleaned}'"
            ) from e

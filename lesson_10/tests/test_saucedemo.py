import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Интернет-магазин")
@allure.story("Сценарий покупки товаров")
class TestSaucedemo:

    @allure.title(
        "Полный сценарий покупки: авторизация → добавление → оформление"
    )
    @allure.description(
        "Проверяем, что итоговая сумма заказа вычисляется корректно"
    )
    @allure.severity(allure.severity_level.BLOCKER)
    def test_saucedemo_full_flow(self, driver):
        with allure.step(
            "Открыть страницу авторизации и войти как standard_user"
        ):
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login("standard_user", "secret_sauce")

        with allure.step(
            "Добавить в корзину 3 товара и запомнить их цены"
        ):
            inventory = InventoryPage(driver)
            # Получаем цены товаров перед добавлением
            backpack_price = inventory.get_item_price("Sauce Labs Backpack")
            bolt_price = inventory.get_item_price("Sauce Labs Bolt T-Shirt")
            onesie_price = inventory.get_item_price("Sauce Labs Onesie")
            expected_subtotal = backpack_price + bolt_price + onesie_price

            inventory.add_backpack()
            inventory.add_bolt_tshirt()
            inventory.add_onesie()

        with allure.step("Перейти в корзину и нажать Checkout"):
            inventory.go_to_cart()
            cart = CartPage(driver)
            cart.proceed_to_checkout()

        with allure.step(
            "Заполнить форму данными (Валентина, Иванова, 665714)"
        ):
            checkout = CheckoutPage(driver)
            checkout.fill_form("Валентина", "Иванова", "665714")

        with allure.step(
            "Получить субтотал, налог и итоговую сумму"
        ):
            subtotal = checkout.get_subtotal()
            tax = checkout.get_tax()
            total = checkout.get_total()

            # Преобразуем в числа
            subtotal_num = float(subtotal.replace("Item total: $", "").strip())
            tax_num = float(tax.replace("Tax: $", "").strip())
            total_num = float(total.replace("Total: $", "").strip())

        with allure.step(
            "Проверить, что субтотал соответствует сумме цен товаров"
        ):
            assert abs(subtotal_num - expected_subtotal) < 0.01, (
                f"Субтотал {subtotal_num} не равен сумме цен"
                f"{expected_subtotal}"
            )

        with allure.step(
            "Проверить, что итоговая сумма = субтотал + налог"
        ):
            assert abs(total_num - (subtotal_num + tax_num)) < 0.01, \
                f"Итог {total_num} не равен сумме {subtotal_num} + {tax_num}"

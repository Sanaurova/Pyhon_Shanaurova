from pages.saucedemo.login_page import LoginPage
from pages.saucedemo.inventory_page import InventoryPage
from pages.saucedemo.cart_page import CartPage
from pages.saucedemo.checkout_page import CheckoutPage


def test_saucedemo_full_flow(driver):
    # 1. Открыть страницу авторизации
    login_page = LoginPage(driver)
    login_page.open()

    # 2. Авторизоваться как standard_user
    login_page.login("standard_user", "secret_sauce")

    # 3. Добавить товары в корзину
    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack()
    inventory_page.add_bolt_tshirt()
    inventory_page.add_onesie()

    # Проверим, что в корзине 3 товара
    assert inventory_page.get_cart_count() == 3, \
        "В корзине должно быть 3 товара"

    # 4. Перейти в корзину
    inventory_page.go_to_cart()

    # 5. Нажать Checkout
    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    # 6. Заполнить форму данными
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form("Валентина", "Иванова", "665714")

    # 7. Прочитать итоговую стоимость
    total_text = checkout_page.get_total()
    # Ожидаемый формат: "Total: $58.29"
    total_value = total_text.replace("Total: ", "").strip()

    # 8. Проверка итоговой суммы
    assert total_value == "$58.29", \
        f"Ожидалось $58.29, получено {total_value}"

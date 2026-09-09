import allure
from pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.story("Проверка арифметических операций")
class TestCalculator:

    @allure.title("Сложение 7 + 8 с задержкой 45 секунд")
    @allure.description(
        "Проверяем, что калькулятор корректно складывает числа "
        "с учётом задержки"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_slow_calculator_addition(self, driver):
        with allure.step("Открыть страницу калькулятора"):
            calc_page = CalculatorPage(driver).open()

        with allure.step("Установить задержку 45 секунд"):
            calc_page.set_delay("45")

        with allure.step("Нажать кнопки: 7, +, 8, ="):
            calc_page.click_seven()
            calc_page.click_plus()
            calc_page.click_eight()
            calc_page.click_equals()

        with allure.step("Ожидать результат '15' на экране"):
            calc_page.wait_for_result("15")

        with allure.step("Проверить, что результат равен 15"):
            assert calc_page.get_result_text() == "15", "Ожидался результат 15"

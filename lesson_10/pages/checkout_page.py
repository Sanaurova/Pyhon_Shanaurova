from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    # Локаторы (существующие)
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    SUBTOTAL_LABEL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX_LABEL = (By.CLASS_NAME, "summary_tax_label")

    def fill_form(self, first_name: str, last_name: str, postal_code: str):
        """
        Заполнить данные о покупателе и перейти к следующему шагу.
        :param first_name: имя
        :param last_name: фамилия
        :param postal_code: почтовый индекс
        :return: экземпляр текущей страницы
        """
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BUTTON)
        self.wait.until(EC.presence_of_element_located(self.TOTAL_LABEL))
        return self

    def get_total(self) -> str:
        """
        Получить итоговую стоимость заказа.
        :return: строка с суммой, например "Total: $58.29"
        """
        return self.get_text(self.TOTAL_LABEL)

    def get_subtotal(self) -> str:
        """
        Получить строку с субтоталом (цена товаров без налога).
        :return: строка вида "Item total: $53.97"
        """
        return self.get_text(self.SUBTOTAL_LABEL)

    def get_tax(self) -> str:
        """
        Получить строку с налогом.
        :return: строка вида "Tax: $4.32"
        """
        return self.get_text(self.TAX_LABEL)

    def finish_order(self) -> "CheckoutPage":
        """Нажать кнопку 'Finish' для завершения заказа."""
        self.click(self.FINISH_BUTTON)
        return self

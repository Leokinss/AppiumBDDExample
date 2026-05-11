from playwright.sync_api import Page
from pages.web.base_page import BasePage


class MyCartPage(BasePage):
    MY_CART_LOCATOR = ".shopping_cart_link"

    def __init__(self, page: Page):
        super().__init__(page)

    def go_to_my_cart_page(self):
        self.click(self.MY_CART_LOCATOR)

    def get_product_locator(self, product_name: str) -> str:
        return f".cart_item:has-text('{product_name}')"

    def is_product_in_cart(self, product_name: str) -> bool:
        return self.is_element_visible(self.get_product_locator(product_name))

from playwright.sync_api import Page
from pages.web.base_page import BasePage


class CatalogPage(BasePage):
    CATALOG_PAGE_TITLE = ".title"

    def __init__(self, page: Page):
        super().__init__(page)

    def is_catalog_page_title_visible(self) -> bool:
        return self.is_element_visible(self.CATALOG_PAGE_TITLE, timeout=5)

    def get_product_selector(self, product_name: str) -> str:
        return f".inventory_item:has-text('{product_name}')"

    def get_add_to_cart_selector(self, product_name: str) -> str:
        return f"{self.get_product_selector(product_name)} button:has-text('Add to cart')"

    def add_to_cart(self, product_name: str) -> None:
        self.click(self.get_add_to_cart_selector(product_name))

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from pages.mobile.base_page import BasePage
from selenium.common.exceptions import TimeoutException


class CatalogPage(BasePage):
    CATALOG_PAGE_TITLE = None
    ADD_TO_CART_BUTTON = None

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_catalog_page_title_visible(self) -> bool:
        try:
            self.find(self.CATALOG_PAGE_TITLE, timeout=5)
            return True
        except TimeoutException:
            return False

    def get_product_by_name(self, product_name: str) -> tuple[AppiumBy, str]:
        raise NotImplementedError

    def add_to_cart(self, product_name: str) -> None:
        raise NotImplementedError

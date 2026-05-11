from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from pages.mobile.base_page import BasePage


class MyCartPage(BasePage):
    MY_CART_LOCATOR = None

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def go_to_my_cart_page(self):
        self.click(self.MY_CART_LOCATOR)

    def get_product_locator(self, product_name: str) -> tuple[AppiumBy, str]:
        raise NotImplementedError

    def is_product_in_cart(self, product_name: str) -> bool:
        locator = self.get_product_locator(product_name)
        return self.is_element_visible(locator)

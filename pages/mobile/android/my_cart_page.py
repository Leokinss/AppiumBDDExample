from appium.webdriver.common.appiumby import AppiumBy
from pages.mobile.my_cart_page import MyCartPage


class AndroidMyCartPage(MyCartPage):
    MY_CART_LOCATOR = (AppiumBy.ACCESSIBILITY_ID, "Displays number of items in your cart")

    def get_product_locator(self, product_name: str) -> tuple[AppiumBy, str]:
        return (AppiumBy.XPATH, f"//*[@text='{product_name}']")

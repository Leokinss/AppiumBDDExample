from appium.webdriver.common.appiumby import AppiumBy
from pages.mobile.catalog_page import CatalogPage


class AndroidCatalogPage(CatalogPage):
    CATALOG_PAGE_TITLE = (AppiumBy.ACCESSIBILITY_ID, "title")
    ADD_TO_CART_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Tap to add product to cart")

    def get_product_by_name(self, product_name: str) -> tuple[AppiumBy, str]:
        return (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{product_name}")',
        )

    def add_to_cart(self, product_name: str) -> None:
        locator = self.get_product_by_name(product_name)

        # move 50 pixels above the element and click because only the image can be clicked
        self.click_offset(locator, y_offset=-50)

        self.click(self.ADD_TO_CART_BUTTON)

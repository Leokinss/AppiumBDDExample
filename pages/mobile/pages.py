from pages.mobile.base_page import BasePage
from pages.mobile.android.catalog_page import AndroidCatalogPage
from pages.mobile.android.login_page import AndroidLoginPage
from pages.mobile.android.my_cart_page import AndroidMyCartPage
from pages.mobile.android.navigation_page import AndroidNavigationPage

PAGE_CLASSES = {
    "Android": {
        "navigation": AndroidNavigationPage,
        "login": AndroidLoginPage,
        "catalog": AndroidCatalogPage,
        "myCart": AndroidMyCartPage,
    },
}


# Container for all page objects to simplify access in tests
class Pages:
    def __init__(self, driver, platform: str):
        if platform not in PAGE_CLASSES:
            available = ", ".join(sorted(PAGE_CLASSES.keys()))
            raise ValueError(
                f"No page objects registered for platform '{platform}'. Available: {available}"
            )
        classes = PAGE_CLASSES[platform]
        self.base = BasePage(driver)
        self.navigation = classes["navigation"](driver)
        self.login = classes["login"](driver)
        self.catalog = classes["catalog"](driver)
        self.myCart = classes["myCart"](driver)

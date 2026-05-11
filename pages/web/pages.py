from playwright.sync_api import Page
from pages.web.base_page import BasePage
from pages.web.catalog_page import CatalogPage
from pages.web.login_page import LoginPage
from pages.web.my_cart_page import MyCartPage
from pages.web.navigation_page import NavigationPage


# Container for all web page objects to simplify access in tests.
class WebPages:
    def __init__(self, page: Page):
        self.base = BasePage(page)
        self.navigation = NavigationPage(page)
        self.login = LoginPage(page)
        self.catalog = CatalogPage(page)
        self.myCart = MyCartPage(page)

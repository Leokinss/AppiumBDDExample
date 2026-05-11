from playwright.sync_api import Page
from pages.web.base_page import BasePage


class NavigationPage(BasePage):
    APP_LOGO_AND_NAME = ".app_logo"
    NAV_BUTTON_MENU = "#react-burger-menu-btn"
    NAV_LOGIN_BUTTON = "#login_sidebar_link"
    NAV_LOGOUT_BUTTON = "#logout_sidebar_link"

    def __init__(self, page: Page):
        super().__init__(page)

    def open_menu(self):
        self.click(self.NAV_BUTTON_MENU)

    def go_to_login_page(self):
        self.open_menu()
        self.click(self.NAV_LOGIN_BUTTON)

    def is_logout_button_visible(self):
        return self.is_element_visible(self.NAV_LOGOUT_BUTTON)

    def is_app_logo_and_name_visible(self):
        return self.is_element_visible(self.APP_LOGO_AND_NAME, timeout=10)

from appium.webdriver.webdriver import WebDriver
from pages.mobile.base_page import BasePage


class NavigationPage(BasePage):
    APP_LOGO_AND_NAME = None
    NAV_BUTTON_MENU = None
    NAV_LOGIN_BUTTON = None
    NAV_LOGOUT_BUTTON = None

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_menu(self):
        self.click(self.NAV_BUTTON_MENU)

    def go_to_login_page(self):
        self.open_menu()
        self.click(self.NAV_LOGIN_BUTTON)

    def is_logout_button_visible(self):
        return self.is_element_visible(self.NAV_LOGOUT_BUTTON)

    def is_app_logo_and_name_visible(self):
        return self.is_element_visible(self.APP_LOGO_AND_NAME, timeout=10)

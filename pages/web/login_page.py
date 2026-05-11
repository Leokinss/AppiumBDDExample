from playwright.sync_api import Page
from pages.web.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_FIELD = "#user-name"
    PASSWORD_FIELD = "#password"
    LOGIN_BUTTON = "#login-button"

    def __init__(self, page: Page):
        super().__init__(page)

    def enter_username(self, username: str) -> None:
        self.send_keys(self.USERNAME_FIELD, username)

    def enter_password(self, password: str) -> None:
        self.send_keys(self.PASSWORD_FIELD, password)

    def tap_login(self) -> None:
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.tap_login()

    def is_error_message_visible(self, text: str, timeout: int = 5) -> bool:
        return self.is_element_visible(f"text={text}", timeout)

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from pages.mobile.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_FIELD = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")
    PASSWORD_FIELD = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET")
    LOGIN_BUTTON = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

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
        locator = (
            AppiumBy.XPATH,
            f'//android.widget.TextView[contains(@resource-id, "ErrorTV") and @text="{text}"]',
        )
        return self.is_element_visible(locator, timeout)
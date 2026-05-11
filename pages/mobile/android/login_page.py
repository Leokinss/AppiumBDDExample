from appium.webdriver.common.appiumby import AppiumBy
from pages.mobile.login_page import LoginPage


class AndroidLoginPage(LoginPage):
    USERNAME_FIELD = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")
    PASSWORD_FIELD = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET")
    LOGIN_BUTTON = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn")

    def is_error_message_visible(self, text: str, timeout: int = 5) -> bool:
        locator = (
            AppiumBy.XPATH,
            f'//android.widget.TextView[contains(@resource-id, "ErrorTV") and @text="{text}"]',
        )
        return self.is_element_visible(locator, timeout)

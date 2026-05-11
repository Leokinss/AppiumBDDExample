from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError


# BasePage provides common methods for all web pages, wrapping Playwright's Page API.
# Locators here are CSS / text / role selector strings (not tuples).
class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def find(self, selector: str, timeout: int = 10):
        try:
            locator = self.page.locator(selector)
            locator.wait_for(timeout=timeout * 1000)
            return locator
        except PlaywrightTimeoutError:
            raise PlaywrightTimeoutError(
                f"❌ [{self.__class__.__name__}] Element not found in {timeout}s: '{selector}'"
            )

    def send_keys(self, selector: str, text: str, timeout: int = 10):
        try:
            self.page.locator(selector).fill(text, timeout=timeout * 1000)
        except PlaywrightTimeoutError:
            raise PlaywrightTimeoutError(
                f"❌ [{self.__class__.__name__}] Unable to send keys to element in {timeout}s: '{selector}'"
            )

    def click(self, selector: str, timeout: int = 10):
        try:
            self.page.locator(selector).click(timeout=timeout * 1000)
        except PlaywrightTimeoutError:
            raise PlaywrightTimeoutError(
                f"❌ [{self.__class__.__name__}] Unable to click element in {timeout}s: '{selector}'"
            )

    def is_element_visible(self, selector: str, timeout: int = 10) -> bool:
        try:
            self.page.locator(selector).wait_for(timeout=timeout * 1000, state="visible")
            return True
        except PlaywrightTimeoutError:
            return False

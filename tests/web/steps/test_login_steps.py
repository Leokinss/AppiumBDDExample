from tests.utils import env
from pytest_bdd import scenarios, when, then, parsers
from tests.web.steps.common_steps import *

scenarios("../../features/login.feature")

USERNAME = env.required_env("VALID_USER")
PASSWORD = env.required_env("VALID_PASSWORD")


@when("I login with valid credentials")
def enter_valid_credentials(web_pages):
    web_pages.login.login(USERNAME, PASSWORD)


@when("I go to the Log In page")
def go_to_login_page(web_pages):
    web_pages.navigation.go_to_login_page()


@when(parsers.parse('I login with username "{username}" and password "{password}"'))
def login_with_credentials(web_pages, username, password):
    web_pages.login.login(username, password)


@then("I should see the Logout button in the navigation menu")
def should_see_logout_button(web_pages):
    web_pages.navigation.open_menu()
    assert web_pages.navigation.is_logout_button_visible(), "Logout button should be visible in the navigation menu"


@then(parsers.parse('I should see the error "{error}"'))
def should_see_error_message(web_pages, error):
    assert web_pages.login.is_error_message_visible(error), (
        f"Expected error message '{error}' to be visible on the page"
    )

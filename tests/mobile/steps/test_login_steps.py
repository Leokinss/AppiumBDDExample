import os
from tests.utils import env
from pytest_bdd import scenarios, given, when, then, parsers
from tests.mobile.steps.common_steps import *
scenarios("../../features/login.feature")

#temp credentials for testing
USERNAME = env.required_env("VALID_USER")
PASSWORD = env.required_env("VALID_PASSWORD")

@when("I login with valid credentials")
def enter_valid_credentials(pages):
    pages.login.login(USERNAME, PASSWORD)

@when("I go to the Log In page")
def go_to_login_page(pages):
    pages.navigation.go_to_login_page()

@when(parsers.parse('I login with username "{username}" and password "{password}"'))
def login_with_credentials(pages, username, password):
    pages.login.login(username, password)

@then("I should see the Logout button in the navigation menu")
def should_see_logout_button(pages):
    pages.navigation.open_menu()
    assert pages.navigation.is_logout_button_visible(), "Logout button should be visible in the navigation menu"  

@then(parsers.parse('I should see the error "{error}"'))
def should_see_error_message(pages, error):
    assert pages.login.is_error_message_visible(error), (
        f"Expected error message '{error}' to be visible on the page"
    )
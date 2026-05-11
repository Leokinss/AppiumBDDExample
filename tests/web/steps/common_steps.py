from pytest_bdd import given, when, then


@given("the app is launched")
def app_is_launched(web_pages):
    assert web_pages.navigation.is_app_logo_and_name_visible(), "App logo and name should be visible"


@when("I open the navigation menu")
def open_menu(web_pages):
    web_pages.navigation.open_menu()


@then("I should see the Catalog page")
def should_see_catalog_page(web_pages):
    assert web_pages.catalog.is_catalog_page_title_visible(), "Catalog page title should be visible"

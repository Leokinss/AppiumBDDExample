import os
from pytest_bdd import scenarios, given, when, then, parsers
from tests.mobile.steps.common_steps import *
scenarios("../../features/add_to_cart.feature")


@when(parsers.parse("I add {product_name} into the cart"))
def add_to_cart(pages, product_name):
    pages.catalog.add_to_cart(product_name)

@when("I go to my cart page")
def go_to_my_cart_page(pages):
    pages.myCart.go_to_my_cart_page()


@then(parsers.parse("I should see {product_name} in the cart"))
def is_product_visible(pages, product_name):
    assert pages.myCart.is_product_in_cart(
        product_name
    ), f"Expected product {product_name!r} to be visible in the cart"

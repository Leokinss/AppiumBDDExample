Feature: Add to Cart

    Scenario Outline: Add a product to the cart
        Given the app is launched
        Then I should see the Catalog page
        When I add <product_name> into the cart
        And I go to my cart page
        Then I should see <product_name> in the cart

        Examples:
        | product_name |
        | Sauce Labs Backpack |
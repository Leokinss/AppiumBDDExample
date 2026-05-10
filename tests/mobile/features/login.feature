Feature: Login

    Scenario: Successful login
        Given the app is launched
        When I go to the Log In page
        And I login with valid credentials
        Then I should see the Catalog page
        And I should see the Logout button in the navigation menu

    Scenario Outline: Unsuccessful login
        Given the app is launched
        When I go to the Log In page
        And I login with username "<username>" and password "<password>"
        Then I should see the error "<error>"

        Examples:
            | username                            | password     | error                               |
            | alice@example.com (locked out)      | secret_sauce | Sorry this user has been locked out. |
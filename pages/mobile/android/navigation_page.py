from appium.webdriver.common.appiumby import AppiumBy
from pages.mobile.navigation_page import NavigationPage


class AndroidNavigationPage(NavigationPage):
    APP_LOGO_AND_NAME = (AppiumBy.ACCESSIBILITY_ID, "App logo and name")
    NAV_BUTTON_MENU = (AppiumBy.ACCESSIBILITY_ID, "View menu")
    NAV_LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Login Menu Item")
    NAV_LOGOUT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Logout Menu Item")

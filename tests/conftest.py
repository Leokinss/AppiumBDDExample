import os
import sys
import pytest
import yaml
from pathlib import Path
from dotenv import load_dotenv
from appium import webdriver
from appium.options.common import AppiumOptions
# Ensure project root is on sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))
from pages.mobile.pages import Pages
from pages.web.pages import WebPages

CONFIG_PATH = PROJECT_ROOT / "config" / "capabilities.yaml"
APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'
WEB_BASE_URL = os.environ.get("WEB_BASE_URL", "https://www.saucedemo.com/")
PLATFORMS = ["ANDROID", "IOS", "WEB"]
MOBILE_PLATFORMS = {"ANDROID", "IOS"}

load_dotenv(PROJECT_ROOT / "credentials.env")

def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        action="store",
        default="ANDROID",
        help=f"Platform to test on. Supported: {', '.join(PLATFORMS)}. Default: ANDROID",
    )


def pytest_configure(config):
    platform = config.getoption("--platform").upper()
    if platform not in PLATFORMS:
        raise pytest.UsageError(
            f"--platform={platform} is not supported. Choose one of: {', '.join(PLATFORMS)}."
        )


def pytest_collection_modifyitems(config, items):
    # Drop tests that don't belong to the active platform so their fixtures
    # (appium_driver, pytest-playwright's page, etc.) are never instantiated.
    platform = config.getoption("--platform").upper()
    skip_segment = os.sep + ("web" if platform in MOBILE_PLATFORMS else "mobile") + os.sep
    deselected, remaining = [], []
    for item in items:
        if skip_segment in str(item.fspath):
            deselected.append(item)
        else:
            remaining.append(item)
    if deselected:
        config.hook.pytest_deselected(items=deselected)
        items[:] = remaining


# Normalize the app path to handle spaces and relative paths, especially on Windows
def _normalize_app_path(app_path: str) -> str:
    path = Path(app_path)

    if not path.is_absolute():
        path = Path(__file__).parent / path

    return str(path.resolve())


def load_capabilities(device: str = "ANDROID"):
    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        capabilities = yaml.safe_load(file)

    key = f"{device.upper()}_CAPABILITIES"
    if key not in capabilities:
        available = ", ".join(sorted(capabilities.keys()))
        raise ValueError(
            f"Unsupported device '{device}'. Available capabilities: {available}"
        )

    caps = capabilities[key]
    if "app" in caps:
        caps["app"] = _normalize_app_path(caps["app"])

    return caps


@pytest.fixture
def appium_driver(request):
    device = request.config.getoption("--platform")
    caps = load_capabilities(device)

    options = AppiumOptions()
    options.load_capabilities(caps)

    driver = webdriver.Remote(f"http://{APPIUM_HOST}:{APPIUM_PORT}", options=options)
    yield driver
    driver.quit()

@pytest.fixture
def pages(appium_driver):
    platform = appium_driver.capabilities.get("platformName")
    return Pages(appium_driver, platform)

@pytest.fixture
def web_pages(page):
    page.goto(WEB_BASE_URL)
    return WebPages(page)

@pytest.fixture(autouse=True)
def setup_teardown():
    # Setup code before each test
    print("\nSetting up the test environment")
    yield
    # Teardown code after each test
    print("\nTearing down the test environment")

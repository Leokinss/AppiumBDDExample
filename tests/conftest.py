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

CONFIG_PATH = PROJECT_ROOT / "config" / "capabilities.yaml"
APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'

load_dotenv(PROJECT_ROOT / "credentials.env")

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
    
import pytest

@pytest.fixture
def appium_driver():
    device = os.environ.get("TEST_DEVICE", "ANDROID")
    caps = load_capabilities(device)

    options = AppiumOptions()
    options.load_capabilities(caps)

    driver = webdriver.Remote(f"http://{APPIUM_HOST}:{APPIUM_PORT}", options=options)
    yield driver
    driver.quit()

@pytest.fixture
def pages(appium_driver):
    return Pages(appium_driver)

@pytest.fixture(autouse=True)
def setup_teardown(appium_driver):
    # Setup code before each test
    print("\nSetting up the test environment")
    yield
    # Teardown code after each test
    print("\nTearing down the test environment")
import pytest
from playwright.sync_api import sync_playwright, Page, expect

# Helper function to perform login on ThingsBoard demo site
def login(page, username, password):
    page.goto("https://demo.thingsboard.io/login")
    page.fill("input[formcontrolname='username']", username)
    page.fill("input[formcontrolname='password']", password)
    page.click("button[type='submit']")

# Helper function to print widget count if visible
def get_widget_count(page, selector, label):
    count_locator = page.locator(selector)
    if count_locator.is_visible():
        print(f"{label}: {count_locator.inner_text()}")

# Validate the Devices widget is present and print its counts
def validate_devices_widget(page):
    # Check for Devices widget visibility
    devices_widget = page.locator("a[href='/entities/devices']:has-text('Devices')")
    assert devices_widget.is_visible(), "Devices widget not found"
    print("Devices widget is visible")
    # Print total and active device counts
    get_widget_count(page, "a[href*='devices']:has-text('Total') .tb-count", "Total devices")
    get_widget_count(page, "a[href*='devices']:has-text('Active') .tb-count", "Active devices")

# Validate the Alarms widget is present and print its counts
def validate_alarms_widget(page):
    # Check for Alarms widget visibility
    alarms_widget = page.locator("a[href='/alarms']:has-text('Alarms')")
    assert alarms_widget.is_visible(), "Alarms widget not found"
    print("Alarms widget is visible")
    # Print critical and total alarm counts
    get_widget_count(page, "a[href*='alarms']:has-text('Critical') .tb-count", "Critical alarms")
    get_widget_count(page, "a[href='/alarms']:has-text('Total') .tb-count", "Total alarms")

@pytest.mark.ui
def test_validate_devices_and_alarms_widgets(page, credentials):
    """
    UI Test: Validate Devices and Alarms widgets on the dashboard.
    Steps:
    1. Login to the ThingsBoard demo site.
    2. Wait for dashboard widgets to load.
    3. Validate Devices widget and print counts.
    4. Validate Alarms widget and print counts.
    """
    username, password = credentials
    # Step 1: Login
    login(page, username, password)
    # Step 2: Wait for widgets to load
    page.wait_for_selector(".tb-widget", timeout=15000)
    # Step 3: Validate Devices widget
    validate_devices_widget(page)
    # Step 4: Validate Alarms widget
    validate_alarms_widget(page)

from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def Checkdevicewidget(self):
        device1_link = self.page.locator("a.tb-home-widget-title.tb-home-widget-link[href='/entities/devices']")
        device1_link.wait_for(state="visible", timeout=10000)
        assert device1_link.is_visible(), "Devices widget not found"
        print("Devices widget is visible")

    def checkalarmwidget(self):
        self.page.wait_for_timeout(5000)  # Wait for 2 seconds
        alerts1_link = self.page.locator("a.tb-home-widget-title.tb-home-widget-link[href='/alarms']")
        assert alerts1_link.is_visible(), "Alarm widget not found"
        print("Alarms widget is visible")
# filepath: c:\MyTestProject\ProjectFly\pages\thingsboard_api_page.py
import requests
from playwright.sync_api import Page, expect
# This class encapsulates API interactions with Thingsboard
# It provides methods to fetch telemetry keys and latest telemetry data for a specific device
class ThingsboardApiPage:
    # Constructor to initialize the API page with base URL, device ID, and headers
    def __init__(self, base_url, device_id, headers):
        self.base_url = base_url # Base URL for the Thingsboard API
        self.device_id = device_id # Device ID for which telemetry data is to be fetched
        self.headers = headers # Headers to be used in API requests, typically for authentication
# This method retrieves the telemetry keys for the specified device
    def get_telemetry_keys(self):
        url = f"{self.base_url}/api/plugins/telemetry/DEVICE/{self.device_id}/keys/timeseries" # Construct the URL for fetching telemetry keys
        # Make a GET request to the Thingsboard API to retrieve telemetry keys
        resp = requests.get(url, headers=self.headers)
        # Check if the response was successful
        resp.raise_for_status()
        return resp.json()
# This method retrieves the latest telemetry data for the specified device
    def get_latest_telemetry(self):
        # Construct the URL for fetching the latest telemetry data
        url = f"{self.base_url}/api/plugins/telemetry/DEVICE/{self.device_id}/values/timeseries?keys=temperature,pressure"
        resp = requests.get(url, headers=self.headers)
        resp.raise_for_status()
        return resp.json()
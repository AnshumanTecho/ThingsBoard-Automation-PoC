import pytest
import requests

# -------------------- Constants --------------------

BASE_URL = "https://demo.thingsboard.io"
LOGIN_URL = f"{BASE_URL}/api/auth/login"
TELEMETRY_KEYS_URL = f"{BASE_URL}/api/plugins/telemetry/DEVICE/{{device_id}}/keys/timeseries"
TELEMETRY_DATA_URL = f"{BASE_URL}/api/plugins/telemetry/DEVICE/{{device_id}}/values/timeseries?keys=temperature,pressure"
DEVICE_ID = "8582e7e0-5277-11f0-9664-ff13eccb47ff"

# -------------------- Test Cases --------------------

def test_get_telemetry_keys(headers):
    url = TELEMETRY_KEYS_URL.format(device_id=DEVICE_ID)
    resp = requests.get(url, headers=headers)
    assert resp.status_code == 200, f"Failed to fetch telemetry keys: {resp.text}"
    keys = resp.json()
    print("Telemetry keys:", keys)
    assert isinstance(keys, list), "Expected a list of telemetry keys"
    assert any(k in keys for k in ["temperature", "pressure"]), "Expected telemetry keys not found"

def test_fetch_latest_telemetry(headers):
    url = TELEMETRY_DATA_URL.format(device_id=DEVICE_ID)
    resp = requests.get(url, headers=headers)
    assert resp.status_code == 200, f"Telemetry fetch failed: {resp.text}"
    data = resp.json()
    print("Telemetry data:", data)
    assert any(k in data for k in ["temperature", "pressure"]), "Telemetry data missing"
    for key in ["temperature", "pressure"]:
        if key in data:
            assert isinstance(data[key], list) and len(data[key]) > 0, f"No data points for {key}"
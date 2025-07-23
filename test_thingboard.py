from playwright.sync_api import expect
from pages.thingsboard_home_page import HomePage
#from pages.thingboard_login_page import Thingsboardloginpage
from utils import login
from pages.thingsboard_api_page import ThingsboardApiPage


#first test function to check login functionality
# test function to check home page info
def test_home_page_ifo(page, credentials):# test function to check home page info(page, credentials):
    #calling page url and credentials from conftest.py
    login(page, "https://demo.thingsboard.io/login", *credentials) #calling the login function from utils.py
   #calling objecthome page from thingsboard_home_page.py
    t_home_page = HomePage(page)  #calling the HomePage class from thingsboard_home_page.py
    t_home_page.Checkdevicewidget() #calling the method to check device widget
    t_home_page.checkalarmwidget() #calling the method to check alaram widget
    
    
    
 
#second Test function to check telemetry data
BASE_URL = "https://demo.thingsboard.io"
DEVICE_ID = "8582e7e0-5277-11f0-9664-ff13eccb47ff"

def test_api_telemetry(headers):
    api_page = ThingsboardApiPage(BASE_URL, DEVICE_ID, headers)
    
    # Test telemetry keys
    keys = api_page.get_telemetry_keys()
    print("Telemetry keys:", keys)
    assert isinstance(keys, list), "Expected a list of telemetry keys"
    assert any(k in keys for k in ["temperature", "pressure"]), "Expected telemetry keys not found"

    # Test latest telemetry data
    data = api_page.get_latest_telemetry()
    print("Telemetry data:", data)
    assert any(k in data for k in ["temperature", "pressure"]), "Telemetry data missing"
    for key in ["temperature", "pressure"]:
        if key in data:
            assert isinstance(data[key], list) and len(data[key]) > 0, f"No data points for {key}"   
 
    
    
    


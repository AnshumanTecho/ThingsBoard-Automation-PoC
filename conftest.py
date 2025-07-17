import pytest  
import requests  
import os  
import pandas as pd  
from utils import get_credentials_from_sheet  

BASE_URL = "https://demo.thingsboard.io"  # Define the base URL for the ThingsBoard API
LOGIN_URL = f"{BASE_URL}/api/auth/login"  # Define the login endpoint URL

@pytest.fixture(scope="session")  # Define a pytest fixture with session scope (runs once per session)
def credentials():
    return get_credentials_from_sheet()  # Retrieve credentials from an external source

# -------------------- Fixtures for API call --------------------

@pytest.fixture(scope="session")  # Define a session-scoped fixture for authentication
def auth_token(credentials):
    """
    Authenticate with the ThingsBoard API and return a JWT token.
    This fixture runs once per test session.
    """
    username, password = credentials  # Unpack the username and password from credentials
    resp = requests.post(LOGIN_URL, json={"username": username, "password": password})  # Send a POST request to the login endpoint with credentials
    resp.raise_for_status()  # Raise an HTTPError if the authentication request failed
    token = resp.json().get("token")  # Extract the JWT token from the JSON response
    assert token, "Authentication failed: No token received"  # Ensure a token was received, else fail the test
    return token  # Return the JWT token for use in other tests

@pytest.fixture(scope="session")  # Define a session-scoped fixture for HTTP headers
def headers(auth_token):
    """
    Return HTTP headers including the authorization token.
    Used for all authenticated API requests.
    """
    return {
        "X-Authorization": f"Bearer {auth_token}",  # Set the authorization header with the JWT token
        "Content-Type": "application/json"  # Set the content type to JSON
    }
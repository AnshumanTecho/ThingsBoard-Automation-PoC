# thingsboard_full_setup Automation Test Suite

This repository demonstrates how to run UI and API automation tests using Python, Pytest, Playwright, and Requests.

---

## Prerequisites

- [Python](https://www.python.org/downloads/) (3.7+)
- [pip](https://pip.pypa.io/en/stable/installation/)

## Libraries Used

- [pytest](https://docs.pytest.org/en/stable/) &mdash; Test framework for Python
- [playwright](https://playwright.dev/python/) &mdash; Browser automation library
- [requests](https://docs.python-requests.org/en/latest/) &mdash; HTTP library for API testing

## Setup

1. **Clone the repository**
    ```bash
    git clone <repository-url>
    cd ProjectFly
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    playwright install
    ```

## Running Tests

### UI Tests

To run browser-based UI automation:

```bash
pytest tests/ui/test_dashboard_ui.py --html=ui-report.html
```

- Open `ui-report.html` in your browser to view results.

### API Tests

To run API automation:

```bash
pytest tests/api/test_api.py --html=api-report.html
```

- Open `api-report.html` in your browser to view results.

---

## Additional Information

- This project is for demonstration and proof-of-concept use.
- For questions or issues, open an issue in this repository.
- For debugging, refer to the Pytest and Playwright documentation.
- For IoT-related test information, see the relevant test files or documentation in the `tests/iot/` directory if available.


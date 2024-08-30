import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.fixture(scope="class")
def setup(request):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    request.cls.page = page
    yield page

    context.close()
    browser.close()
    playwright.stop()

@pytest.fixture(scope="function")
def login_page(setup):
    return LoginPage(setup)

@pytest.fixture(scope="function")
def dashboard_page(setup):
    return DashboardPage(setup)

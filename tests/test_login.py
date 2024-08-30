import pytest
import allure

@pytest.mark.usefixtures("setup")
class TestLogin:

    @allure.title("Test Login - Successful")
    @allure.description("This test verifies that a user can log in with valid credentials.")
    def test_login_successfully(self, login_page, dashboard_page):
        login_page.open_page()
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()

        assert dashboard_page.is_dashboard_displayed()

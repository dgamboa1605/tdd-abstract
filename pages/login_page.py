from pages.base_page import BasePage


class LoginPage(BasePage):
    
    def open_page(self):
        """Open the login page"""
        self.page.goto("https://www.saucedemo.com")
    
    def enter_username(self, username: str):
        self.page.fill("#user-name", username)
    
    def enter_password(self, password: str):
        self.page.fill("#password", password)
    
    def click_login_button(self):
        self.page.click("#login-button")


from pages.base_page import BasePage


class DashboardPage(BasePage):
    
    def open_page(self):
        """Open the dashboard page (typically, this would redirect after login)"""
        self.page.goto("https://www.saucedemo.com/inventory.html")
    
    def is_dashboard_displayed(self) -> bool:
        """Check if the dashboard is displayed"""
        return self.page.is_visible(".app_logo")

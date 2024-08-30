from abc import ABC, abstractmethod
from playwright.sync_api import Page

class BasePage(ABC):
    
    def __init__(self, page: Page) -> None:
        self.page = page
    
    @abstractmethod
    def open_page(self):
        """
        Open the page URL
        """
        pass
    
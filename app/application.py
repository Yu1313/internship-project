from pages.base_page import Page
from pages.main_menu_page import MainMenuPage
from pages.signin_page import SigninPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_menu_page = MainMenuPage(driver)
        self.signin_page = SigninPage(driver)


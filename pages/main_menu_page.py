from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainMenuPage(Page):
    MAIN_MENU = (By.CSS_SELECTOR, "[class='menu-button-block link-block link-block-2 link-block-3 link-block-4 w-inline-block w--current']")
    EN_LANG_SELECTION = (By.CSS_SELECTOR, "#w-dropdown-toggle-0")
    RU_LANG_SELECTION = (By. CSS_SELECTOR, "[lang='ru']")
    RU_LANG_TXT = (By. CSS_SELECTOR, "//h1[text()='Главное меню']")

    def click_main_menu(self):
        self.wait_and_click(*self.MAIN_MENU)

    def select_en_language(self):
        self.wait_and_click(*self.EN_LANG_SELECTION)

    def select_ru_language(self):
        self.wait_and_click(*self.RU_LANG_SELECTION)

    def verify_ru_language_change(self):
        self.wait_for_element_appear(*self.RU_LANG_TXT)
        self.verify_text('Главное меню', *self.RU_LANG_TXT)









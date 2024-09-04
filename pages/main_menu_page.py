from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class MainMenuPage(Page):
    MAIN_MENU = (By.CSS_SELECTOR, 'div[class*="menu_grid"] a[href="/main-menu"]')
    EN_LANG_SELECTION = (By.CSS_SELECTOR, "#w-dropdown-toggle-0")
    RU_LANG_SELECTION = (By. CSS_SELECTOR, "[class='wg-dropdown-1-link-2 w-dropdown-link']")
    RU_LANG_TXT = (By. XPATH, "//h1[text()='Главное меню']")

    def click_main_menu(self):
        self.wait_and_click(*self.MAIN_MENU)

    def select_en_language(self):
        hover_dd = self.find_element(*self.EN_LANG_SELECTION)

        actions = ActionChains(self.driver)
        actions.move_to_element(hover_dd)
        actions.perform()
        sleep(3)

    def select_ru_language(self):
        self.wait_and_click(*self.RU_LANG_SELECTION)

    def verify_ru_language_change(self):
        self.wait_for_element_appear(*self.RU_LANG_TXT)
        self.verify_text('Главное меню', *self.RU_LANG_TXT)










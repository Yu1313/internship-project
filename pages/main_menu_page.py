from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class MainMenuPage(Page):
    MAIN_MENU_WEB = (By.CSS_SELECTOR, 'div[class*="menu_grid"] a[href="/main-menu"]')
    MAIN_MENU_MOBILE = (By.CSS_SELECTOR, "[href='/main-menu']")
    EN_LANG_SELECTION_WEB = (By.CSS_SELECTOR, "#w-dropdown-toggle-0")
    EN_LANG_SELECTION_MOBILE = (By.CSS_SELECTOR, "#w-dropdown-toggle-0")
    RU_LANG_SELECTION_WEB = (By. CSS_SELECTOR, "[class='wg-dropdown-1-link-2 w-dropdown-link']")
    RU_LANG_TXT = (By. XPATH, "//h1[text()='Главное меню']")

    def click_main_menu_web(self):
        self.wait_and_click(*self.MAIN_MENU_WEB)

    def click_main_menu_mobile(self):
        element = self.find_elements(*self.MAIN_MENU_MOBILE)
        element[1].click()
        # self.wait_and_click(*self.MAIN_MENU_MOBILE)

    def select_en_language_web(self):
        hover_dd = self.find_element(*self.EN_LANG_SELECTION_WEB)

        actions = ActionChains(self.driver)
        actions.move_to_element(hover_dd)
        actions.perform()
        sleep(3)

    def select_en_language_mobile(self):
        self.wait_and_click(*self.EN_LANG_SELECTION_MOBILE)
        sleep(2)

    def select_ru_language_web(self):
        self.wait_and_click(*self.RU_LANG_SELECTION_WEB)

    def select_ru_language_mobile(self):
        self.wait_and_click(*self.RU_LANG_SELECTION_WEB)

    def verify_ru_language_change(self):
        self.wait_for_element_appear(*self.RU_LANG_TXT)
        self.verify_text('Главное меню', *self.RU_LANG_TXT)










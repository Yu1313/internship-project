from selenium.webdriver.common.by import By
from pages.base_page import Page


class SigninPage(Page):
    INPUT_EMAIL = (By.CSS_SELECTOR, "[wized='emailInput']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "[wized='passwordInput']")
    CONTINUE_BTN = (By.CSS_SELECTOR, "[wized='loginButton']")

    def open_reelly_signin(self):
        self.open_url('https://soft.reelly.io/sign-in')

    def input_email_and_password(self, email, password):
        self.input_text('importantmnb098@gmail.com', *self.INPUT_EMAIL)
        self.input_text('Password321$', *self.INPUT_PASSWORD)

    def click_continue_btn(self):
        self.wait_and_click(*self.CONTINUE_BTN)

    def verify_logged_in(self):
        self.verify_url('https://soft.reelly.io/')

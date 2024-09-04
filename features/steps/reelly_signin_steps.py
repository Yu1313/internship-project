from selenium.webdriver.common.by import By
from behave import given, when, then


INPUT_EMAIL = (By.CSS_SELECTOR, "[wized='emailInput']")
INPUT_PASSWORD = (By.CSS_SELECTOR, "[wized='passwordInput']")


@given('Open Reelly signin page')
def open_signin_page(context):
    context.app.signin_page.open_reelly_signin()


@when('Enter correct email and password combination')
def input_email_and_password(context):
    context.app.signin_page.input_email_and_password(INPUT_EMAIL, INPUT_PASSWORD)


@when('Click signin button')
def click_signin_button(context):
    context.app.signin_page.click_continue_btn()


@then('Verify user is logged in')
def verify_user_is_logged_in(context):
    context.app.signin_page.verify_logged_in()





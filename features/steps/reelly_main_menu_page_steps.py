from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@when('Click Main Menu nav link')
def click_main_menu_nav(context):
    sleep(1)
    context.app.main_menu_page.click_main_menu()


@when('Click EN language')
def click_en_language(context):
    context.app.main_menu_page.select_en_language()


@when('Click RU language')
def click_ru_language(context):
    context.app.main_menu_page.select_ru_language()


@then('Verify language is changed')
def verify_language_is_changed(context):
    sleep(1)
    context.app.main_menu_page.verify_ru_language_change()







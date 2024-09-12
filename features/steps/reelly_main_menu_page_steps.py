from behave import given, when, then


@when('Click Main Menu web nav link')
def click_main_menu_nav(context):
    context.app.main_menu_page.click_main_menu_web()


@when('Click Main Menu mobile nav link')
def click_main_menu_nav(context):
    context.app.main_menu_page.click_main_menu_mobile()


@when('Click EN language')
def click_en_language(context):
    context.app.main_menu_page.select_en_language_web()


@when('Click EN language mobile dropdown')
def click_en_language(context):
    context.app.main_menu_page.select_en_language_mobile()


@when('Click RU language')
def click_ru_language(context):
    context.app.main_menu_page.select_ru_language_web()


@when('Click RU language mobile dropdown')
def click_ru_language(context):
    context.app.main_menu_page.select_ru_language_mobile()


@then('Verify language is changed')
def verify_language_is_changed(context):
    context.app.main_menu_page.verify_ru_language_change()







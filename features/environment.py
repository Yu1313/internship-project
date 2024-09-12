from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from support.logger import logger
from app.application import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # # Mobile emulation, Setup Chrome options for mobile emulation
    # chrome_options = Options()
    # mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #
    # # Initialize Chrome WebDriver with mobile emulation
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service, options=chrome_options)

    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ## HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    # options.add_argument('--window-size=1920x1080')
    # service = Service(GeckoDriverManager().install())
    # context.driver = webdriver.Firefox(
    #     options=options,
    #     service=service
    # )

    # ### BROWSERSTACK ###
    # # Web Config
    # bs_user = 'yus_v62daS'
    # bs_key = 'V2UYdzzPtNCZJUCxB5qW'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # options = Options()
    # bstack_options = {
    #     'os': 'OS X',
    #     'osVersion': 'Ventura',
    #     'browserName': 'Safari',
    #     "browserVersion": "16.5",
    #     "seleniumVersion": "4.21.0",
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    # Mobile config
    bs_user = 'yus_v62daS'
    bs_key = 'V2UYdzzPtNCZJUCxB5qW'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    options = Options()
    bstack_options = {
        'osVersion': '17',
        'deviceName': "iPhone 12",
        'browserName': 'Safari',
        'sessionName': scenario_name
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):  # called hooks
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    logger.info(f'Started step: {step}')
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()

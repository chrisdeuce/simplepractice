import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture(scope='session')
def config():
    with open('config.json') as config_file:
        config = json.load(config_file)

    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome', 'Headless Firefox'], \
        f"Unsupported browser: {config['browser']}"
    assert isinstance(config['implicit_wait'], int) and config['implicit_wait'] > 0, \
        "implicit_wait must be a positive integer"

    return config

@pytest.fixture
def browser(config):
    browser_name = config['browser']
    implicit_wait = config['implicit_wait']

    if browser_name == 'Firefox':
        options = FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService(), options=options)

    elif browser_name == 'Chrome':
        options = ChromeOptions()
        driver = webdriver.Chrome(service=ChromeService(), options=options)

    elif browser_name == 'Headless Chrome':
        options = ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(service=ChromeService(), options=options)

    elif browser_name == 'Headless Firefox':
        options = FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(service=FirefoxService(), options=options)

    else:
        raise Exception(f'Browser "{browser_name}" is not supported')

    driver.implicitly_wait(implicit_wait)
    driver.maximize_window()
    yield driver
    driver.quit()
import pytest
import requests
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from email_log import send_log_to_email

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']
    log_email = testdata['log_email']
    log_pass = testdata['log_email_pass']
    log_file = testdata['log_name']
    html_report = testdata['html_report']
    api_address = testdata['address_login_API']
    username = testdata['login']
    password = testdata['password']

S = requests.Session()


@pytest.fixture(scope='session')
def browser_input():
    if browser == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    send_log_to_email(log_email, log_email, log_pass, log_file, html_report)
    driver.quit()


@pytest.fixture(scope='session')
def get_api_token():
    token = S.post(url=api_address, data={'username': username, 'password': password})
    return token.json()['token']

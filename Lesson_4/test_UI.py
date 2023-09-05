import time
import logging
import yaml
from testpage import OperationsHelper

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_login_negative(browser_input):
    logging.info("Test_login_negative started.")
    testpage = OperationsHelper(browser_input)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == '401'


def test_login_positive(browser_input):
    logging.info("Test_login_positive started.")
    testpage = OperationsHelper(browser_input)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    assert testpage.get_greeting() == f"Hello, {testdata['login']}"


def test_create_post(browser_input):
    # Нажать кнопку "Create new post"
    logging.info("Test_create_post started.")
    testpage = OperationsHelper(browser_input)
    testpage.click_new_post_button()
    time.sleep(testdata['sleep_time'])
    # Заполнить поля
    testpage.enter_post_title(testdata['post_title'])
    testpage.enter_post_description(testdata['post_description'])
    testpage.enter_post_content(testdata['post_content'])
    # Нажать кнопку "Save"
    testpage.click_save_post_button()
    time.sleep(testdata['sleep_time'])
    # Проверить наличие поста на странице
    assert testpage.get_new_post_title() == testdata['post_title']


def test_contact(browser_input):
    # Нажать кнопку "Contact"
    logging.info("Test contact started.")
    testpage = OperationsHelper(browser_input)
    testpage.click_contact_button()
    time.sleep(testdata['sleep_time'])
    # Заполнить поля
    testpage.enter_contact_name(testdata['login'])
    testpage.enter_contact_email(testdata['email'])
    testpage.enter_contact_content(testdata['contact_content'])
    # Нажать кнопку "Save"
    testpage.click_contact_send_button()
    time.sleep(testdata['sleep_time'])
    # Проверить наличие алерта на странице
    assert testpage.get_alert() == testdata['alert_text']

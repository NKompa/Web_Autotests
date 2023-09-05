from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestSearchLocators:
    ids = dict()
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while getting text from {element_name}")
            return None
        logging.debug(f"We found text {text} in field {locator}")
        return text

    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description='login field')

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description='password field')

    def enter_post_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_POST_TITLE"], word, description='post title field')

    def enter_post_description(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_POST_DESCRIPTION"], word,
                                   description='post description field')

    def enter_post_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_POST_CONTENT"], word,
                                   description='post content field')

    def enter_contact_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_YOUR_NAME"], word,
                                   description='contact name field')

    def enter_contact_email(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_YOUR_EMAIL"], word,
                                   description='contact email field')

    def enter_contact_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT"], word,
                                   description='contact message field')

    # CLICK BUTTON
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description='login button')

    def click_new_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_NEW_POST_BTN"], description='create new post button')

    def click_save_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_POST_BTN"], description='save new post button')

    def click_contact_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description='contact button')

    def click_contact_send_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_SEND_BTN"], description='contact send button')

    # GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description='error text')

    def get_greeting(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_GREETING"], description='greeting text')

    def get_new_post_title(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_NEW_POST_TITLE"],
                                          description='new post expected title')

    def get_alert(self):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text

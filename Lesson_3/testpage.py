from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """/html/body/div/main/div/div/div/form/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """/html/body/div/main/div/div/div/form/div[2]/label/input""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """/html/body/div/main/div/div/div[2]/h2""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
    LOCATOR_GREETING = (By.XPATH, """/html/body/div[1]/main/nav/ul/li[3]/a""")
    LOCATOR_NEW_POST_BTN = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_POST_TITLE = (By.XPATH, """/html/body/div/main/div/div/form/div/div/div[1]/div/label/input""")
    LOCATOR_POST_DESCRIPTION = (By.XPATH, """/html/body/div/main/div/div/form/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_POST_CONTENT = (By.XPATH, """/html/body/div/main/div/div/form/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_POST_BTN = (By.XPATH, """/html/body/div/main/div/div/form/div/div/div[7]/div/button/span""")
    LOCATOR_NEW_POST_TITLE = (By.XPATH, """/html/body/div[1]/main/div/div[1]/h1""")
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_YOUR_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_YOUR_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_SEND_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")

class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_greeting(self):
        greeting_field = self.find_element(TestSearchLocators.LOCATOR_GREETING)
        return greeting_field.text

    def click_new_post_button(self):
        logging.info("Click new post button")
        self.find_element(TestSearchLocators.LOCATOR_NEW_POST_BTN).click()

    def enter_post_title(self, word):
        logging.info(f"Enter title {word} into new post {TestSearchLocators.LOCATOR_POST_TITLE[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE)
        login_field.clear()
        login_field.send_keys(word)

    def enter_post_description(self, word):
        logging.info(f"Enter description {word} into new post {TestSearchLocators.LOCATOR_POST_DESCRIPTION[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_POST_DESCRIPTION)
        login_field.clear()
        login_field.send_keys(word)

    def enter_post_content(self, word):
        logging.info(f"Enter content {word} into new post {TestSearchLocators.LOCATOR_POST_CONTENT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_POST_CONTENT)
        login_field.clear()
        login_field.send_keys(word)

    def click_save_post_button(self):
        logging.info("Click save post button")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_BTN).click()

    def get_new_post_title(self):
        new_post_title = self.find_element(TestSearchLocators.LOCATOR_NEW_POST_TITLE)
        return new_post_title.text

    def click_contact_button(self):
        logging.info("Click contact button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def enter_contact_name(self, word):
        logging.info(f"Enter name {word} into contact field {TestSearchLocators.LOCATOR_YOUR_NAME[1]}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_NAME)
        name_field.clear()
        name_field.send_keys(word)

    def enter_contact_email(self, word):
        logging.info(f"Enter email {word} into contact field {TestSearchLocators.LOCATOR_YOUR_EMAIL[1]}")
        email_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_EMAIL)
        email_field.clear()
        email_field.send_keys(word)

    def enter_contact_content(self, word):
        logging.info(f"Enter content {word} into contact field {TestSearchLocators.LOCATOR_CONTENT[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT)
        content_field.clear()
        content_field.send_keys(word)

    def click_contact_send_button(self):
        logging.info("Click contact send button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_SEND_BTN).click()

    def get_alert(self):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text

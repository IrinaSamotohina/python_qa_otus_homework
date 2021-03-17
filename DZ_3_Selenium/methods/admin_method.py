from DZ_3_Selenium.locators.locators import BasePageLocators


class AdminPage:

    def __init__(self, browser):
        self.browser = browser

    def find_text_field(self):
        text_field = self.browser.find_element(*BasePageLocators.TEXT_FIELDS)
        return text_field

    def find_sumbit_button(self):
        submit_button = self.browser.find_element(*BasePageLocators.SUBMIT_BUTTON)
        return submit_button

    def find_pass_text(self):
        pass_text = self.browser.find_element(*BasePageLocators.FORGOTTEN_PASS)
        return pass_text

    def find_input_email(self):
        input_email = self.browser.find_element(*BasePageLocators.INPUT_EMAIL)
        return input_email

    def find_alert(self):
        alert = self.browser.find_element(*BasePageLocators.ALERT)
        return alert

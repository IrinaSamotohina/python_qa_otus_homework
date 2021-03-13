from DZ_3_Selenium.locators import BasePageLocators


class AdminPage:

    def __init__(self, browser):
        self.browser = browser

    def find_text_field(self):
        text_field = self.browser.find_element(*BasePageLocators.TEXT_FIELDS)
        return text_field

    def find_sumbit_button(self):
        submit_button = self.browser.find_element(*BasePageLocators.SUBMIT_BUTTON)
        return submit_button

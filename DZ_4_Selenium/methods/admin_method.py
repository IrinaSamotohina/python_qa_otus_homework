from DZ_3_Selenium.locators.locators import AdminPageLocators


class AdminPage:

    def __init__(self, browser):
        self.browser = browser

    def text_field(self):
        find_field = self.browser.find_element(*AdminPageLocators.TEXT_FIELDS)
        find_field.clear()
        text_field = find_field.send_keys("demo")
        return text_field

    def find_and_click_submit_button(self):
        submit_button = self.browser.find_element(*AdminPageLocators.SUBMIT_BUTTON).click()
        return submit_button

    def find_and_click_pass_text(self):
        pass_text = self.browser.find_element(*AdminPageLocators.FORGOTTEN_PASS).click()
        return pass_text

    def find_input_email(self):
        input_email = self.browser.find_element(*AdminPageLocators.INPUT_EMAIL)
        key = input_email.send_keys("test@test.ru")
        return key

    def find_alert(self):
        alert = self.browser.find_element(*AdminPageLocators.ALERT)
        return alert

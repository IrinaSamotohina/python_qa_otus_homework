from DZ_3_Selenium.locators.locators import BasePageLocators


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def find_product_card(self):
        return len(self.browser.find_elements(*BasePageLocators.PRODUCT))

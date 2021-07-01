from DZ_3_Selenium.locators.locators import CatalogPageLocators


class CatalogPage:

    def __init__(self, browser):
        self.browser = browser

    def find_catalog_card(self):
        catalog_card = len(self.browser.find_elements(*CatalogPageLocators.PRODUCT_CATALOG))
        return catalog_card

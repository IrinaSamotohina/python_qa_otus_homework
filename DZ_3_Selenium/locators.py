from selenium.webdriver.common.by import By


class BasePageLocators(object):

    TEXT_FIELDS = (By.CLASS_NAME, "form-control")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
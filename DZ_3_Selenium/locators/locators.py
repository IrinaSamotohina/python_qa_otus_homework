from selenium.webdriver.common.by import By


class BasePageLocators(object):

    TEXT_FIELDS = (By.CLASS_NAME, "form-control")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_PASS = (By.LINK_TEXT, "Forgotten Password")
    INPUT_EMAIL = (By.ID, "input-email")
    ALERT = (By.CLASS_NAME, "alert-dismissible")
    

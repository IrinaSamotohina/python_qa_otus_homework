from selenium.webdriver.common.by import By


class BasePageLocators(object):

    LOGO = (By.ID, "logo")
    SLIDER = (By.ID, "slideshow0")
    BUTTON = (By.CSS_SELECTOR, "button[type='button']")
    TEXT_MAC = (By.LINK_TEXT, "MacBook")
    CURRENCY = (By.XPATH, "//form[@id='form-currency']")
    PRODUCT = (By.CLASS_NAME, "product-thumb")


class CatalogPageLocators(object):

    DROPDOWN_TOGGLE = (By.CLASS_NAME, "dropdown-toggle")
    HOME_BUTTON = (By.CLASS_NAME, "fa-home")
    BUTTON = (By.CSS_SELECTOR, "button[type='button']")
    TEXT_HP = (By.LINK_TEXT, "HP LP3065")
    CURRENCY = (By.XPATH, "//form[@id='form-currency']")
    PRODUCT_CATALOG = (By.CLASS_NAME, "product-thumb")


class AdminPageLocators(object):

    TEXT_FIELDS = (By.CLASS_NAME, "form-control")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_PASS = (By.LINK_TEXT, "Forgotten Password")
    INPUT_EMAIL = (By.ID, "input-email")
    INPUT_USER = (By.ID, "input-username")
    INPUT_PASSWORD = (By.NAME, "password")
    ALERT = (By.CLASS_NAME, "alert-dismissible")
    OPEN_CART = (By.XPATH, "//*[text()='OpenCart']")


class ProductPageLocators(object):

    LIST_UNSTYLED = (By.CLASS_NAME, "list-unstyled")
    BUTTON_CART = (By.ID, "button-cart")
    QUANTITY = (By.NAME, "quantity")
    CART_TEXT = (By.LINK_TEXT, "Samsung Galaxy Tab 10.1")
    LOGO = (By.ID, "logo")


class LoginPageLocators(object):

    ITEMS = (By.ID, "cart-total")
    FIELD_EMAIL = (By.NAME, "email")
    FIELD_PASSWORD = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    CONTINUE_BUTTON = (By.LINK_TEXT, "Continue")

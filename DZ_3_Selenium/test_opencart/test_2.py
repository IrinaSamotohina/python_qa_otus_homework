from DZ_3_Selenium.locators.locators import BasePageLocators
from DZ_3_Selenium.locators.locators import CatalogPageLocators
from DZ_3_Selenium.locators.locators import AdminPageLocators
from DZ_3_Selenium.locators.locators import ProductPageLocators
from DZ_3_Selenium.locators.locators import LoginPageLocators


def test_homepage(browser, open_opencart_homepage):
    # Ищем элементы на главной странице
    product_count = open_opencart_homepage.find_product_card()
    assert product_count == 4
    assert browser.find_element(*BasePageLocators.LOGO)
    assert browser.find_element(*BasePageLocators.SLIDER)
    assert browser.find_element(*BasePageLocators.BUTTON)
    assert browser.find_element(*BasePageLocators.TEXT_MAC)
    assert browser.find_element(*BasePageLocators.CURRENCY)
    assert browser.find_element(*BasePageLocators.PRODUCT)


def test_catalog(browser, open_catalog_page):
    # Ищем элементы на странице каталога
    product_count = open_catalog_page.find_catalog_card()
    assert product_count == 12
    assert browser.find_element(*CatalogPageLocators.DROPDOWN_TOGGLE)
    assert browser.find_element(*CatalogPageLocators.HOME_BUTTON)
    assert browser.find_element(*CatalogPageLocators.BUTTON)
    assert browser.find_element(*CatalogPageLocators.TEXT_HP)
    assert browser.find_element(*CatalogPageLocators.CURRENCY)
    assert browser.find_element(*CatalogPageLocators.PRODUCT_CATALOG)


def test_login_admin_page(browser, admin_login_page):
     # Ищем элементы на странице логина в админку
    assert browser.find_element(*AdminPageLocators.INPUT_USER)
    assert browser.find_element(*AdminPageLocators.INPUT_PASSWORD)
    assert browser.find_element(*AdminPageLocators.SUBMIT_BUTTON)
    assert browser.find_element(*AdminPageLocators.FORGOTTEN_PASS)
    assert browser.find_element(*AdminPageLocators.OPEN_CART)


def test_product_cart(browser, open_product_cart):
    # Ищем элементы на странице карточки товара
    assert browser.find_element(*ProductPageLocators.CART_TEXT)
    assert browser.find_element(*ProductPageLocators.LIST_UNSTYLED)
    assert browser.find_element(*ProductPageLocators.BUTTON_CART)
    assert browser.find_element(*ProductPageLocators.QUANTITY)
    assert browser.find_element(*ProductPageLocators.CART_TEXT)
    assert browser.find_element(*ProductPageLocators.LOGO)


def test_login_page(browser, open_login_page):
    # Ищем элементы на странице логина
    assert browser.find_element(*LoginPageLocators.ITEMS)
    assert browser.find_element(*LoginPageLocators.FIELD_EMAIL)
    assert browser.find_element(*LoginPageLocators.FIELD_PASSWORD)
    assert browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
    assert browser.find_element(*LoginPageLocators.CONTINUE_BUTTON)

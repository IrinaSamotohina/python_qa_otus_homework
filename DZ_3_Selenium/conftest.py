from selenium import webdriver
import pytest
from DZ_3_Selenium.methods.admin_method import AdminPage
from DZ_3_Selenium.methods.base_method import BasePage
from DZ_3_Selenium.methods.catalog_method import CatalogPage


def pytest_addoption(parser):
    parser.addoption("--browser", choices=["chrome", "firefox", "ie"], help="Choose browser")
    parser.addoption("--baseurl", default="https://demo.opencart.com")


@pytest.fixture(scope='session')
def browser(request):
    browser = request.config.getoption("--browser")

    driver = None
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
    elif browser == "ie":
        options = webdriver.IeOptions()
        options.headless = True
        driver = webdriver.Ie(options=options)
        driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture()
def open_opencart_homepage(request, browser):
    browser.get(request.config.getoption("--baseurl"))
    return BasePage(browser)


@pytest.fixture()
def admin_login_page(request, browser):
    browser.get(request.config.getoption("--baseurl") + "/admin/")
    return AdminPage(browser)


@pytest.fixture()
def open_catalog_page(request, browser):
    base_url = request.config.getoption("--baseurl")
    browser.get(base_url + "/index.php?route=product/category&path=20")
    return CatalogPage(browser)


@pytest.fixture()
def open_product_cart(request, browser):
    base_url = request.config.getoption("--baseurl")
    cart = browser.get(base_url + "/index.php?route=product/product&path=57&product_id=49")
    return cart


@pytest.fixture()
def open_login_page(request, browser):
    base_url = request.config.getoption("--baseurl")
    login_page = browser.get(base_url + "/index.php?route=account/login")
    return login_page

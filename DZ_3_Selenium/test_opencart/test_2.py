def test_homepage(browser, open_opencart_homepage):
    # Ищем элементы на главной странице
    browser.get(open_opencart_homepage)
    browser.find_element_by_id("logo")
    browser.find_element_by_id("slideshow0")
    browser.find_element_by_css_selector("button[type='button']")
    browser.find_element_by_link_text("MacBook")
    browser.find_element_by_xpath("//form[@id='form-currency']")
    product_count = len(browser.find_elements_by_class_name("product-thumb"))
    assert product_count == 4


def test_catalog(browser, open_opencart_homepage):
    # Ищем элементы на странице каталога
    browser.get(open_opencart_homepage + "/index.php?route=product/category&path=20")
    browser.find_element_by_class_name("dropdown-toggle")
    browser.find_element_by_class_name("breadcrumb")
    browser.find_element_by_css_selector("button[type='button']")
    browser.find_element_by_link_text("HP LP3065")
    browser.find_element_by_xpath("//form[@id='form-currency']")
    product_catalog = len(browser.find_elements_by_class_name("caption"))
    assert product_catalog == 12


def test_login_admin_page(browser, open_opencart_homepage):
    # Ищем элементы на странице логина в админку
    browser.get(open_opencart_homepage + "/admin/")
    browser.find_element_by_id("input-username")
    browser.find_element_by_name("password")
    browser.find_element_by_css_selector("button[type='submit']")
    browser.find_element_by_link_text("Forgotten Password")
    browser.find_element_by_xpath("//*[text()='OpenCart']")


def test_product_cart(browser, open_opencart_homepage):
    # Ищем элементы на странице карточки товара
    browser.get(open_opencart_homepage + "/index.php?route=product/product&path=57&product_id=49")
    browser.find_element_by_class_name("list-unstyled")
    browser.find_element_by_id("button-cart")
    browser.find_element_by_name("quantity")
    browser.find_element_by_link_text("Samsung Galaxy Tab 10.1")
    browser.find_element_by_id("logo")


def test_login_page(browser, open_opencart_homepage):
    # Ищем элементы на странице логина
    browser.get(open_opencart_homepage + "/index.php?route=account/login")
    browser.find_element_by_id("cart-total")
    browser.find_element_by_name("email")
    browser.find_element_by_name("password")
    browser.find_element_by_css_selector("input[type='submit']")
    browser.find_element_by_link_text("Continue")

from DZ_3_Selenium.base_pages import AdminPage


def test_login_admin(browser, admin_login_page):
    textfield = admin_login_page.find_text_field()
    button = admin_login_page.find_sumbit_button()
    textfield.clear()
    textfield.send_keys("demo")
    button.click()
    assert browser.current_url != 500

# def test_admin_forgotten_password(browser, admin_login_page):
#     browser.get(open_opencart_homepage + "/admin/")
#     browser.find_element_by_link_text("Forgotten Password").click()
#     browser.find_element_by_id("input-email").send_keys("test@test.ru")
#     browser.find_element_by_css_selector("button[type='submit']").click()
#     q = browser.find_element_by_class_name("alert-dismissible")
#     assert q is not None

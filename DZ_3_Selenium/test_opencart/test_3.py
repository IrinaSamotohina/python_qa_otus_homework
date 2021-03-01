def test_login_admin(browser, open_opencart_homepage):
    browser.get(open_opencart_homepage + "/admin/")
    text_fields = browser.find_element_by_class_name("form-control")
    text_fields.clear()
    text_fields.send_keys("demo")
    browser.find_element_by_css_selector("button[type='submit']").click()
    assert browser.current_url is not 500


def test_admin_forgotten_password(browser, open_opencart_homepage):
    browser.get(open_opencart_homepage + "/admin/")
    browser.find_element_by_link_text("Forgotten Password").click()
    browser.find_element_by_id("input-email").send_keys("test@test.ru")
    browser.find_element_by_css_selector("button[type='submit']").click()
    q = browser.find_element_by_class_name("alert-dismissible")
    assert q is not None
def test_login_admin(browser, admin_login_page):
    textfield = admin_login_page.find_text_field()
    button = admin_login_page.find_sumbit_button()
    textfield.clear()
    textfield.send_keys("demo")
    button.click()
    assert browser.current_url != 500


def test_admin_forgotten_password(admin_login_page):
    link = admin_login_page.find_pass_text()
    link.click()
    button = admin_login_page.find_sumbit_button()
    textfield_email = admin_login_page.find_input_email()
    textfield_email.send_keys("test@test.ru")
    button.click()
    q = admin_login_page.find_alert()
    assert q is not None

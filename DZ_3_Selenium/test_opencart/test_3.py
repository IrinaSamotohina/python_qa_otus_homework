def test_login_admin(browser, admin_login_page):
    admin_login_page.text_field()
    admin_login_page.find_and_click_submit_button()
    assert browser.current_url != None


def test_admin_forgotten_password(admin_login_page):
    admin_login_page.find_and_click_pass_text()
    admin_login_page.find_input_email()
    admin_login_page.find_and_click_submit_button()
    assert admin_login_page.find_alert() is not None

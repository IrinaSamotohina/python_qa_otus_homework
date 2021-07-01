def test_first(browser, open_opencart_homepage):
    browser.get(open_opencart_homepage)
    assert browser.current_url == open_opencart_homepage

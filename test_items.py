import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_basket(browser):
    browser.get(link)
    time.sleep(30)
    b_link = browser.find_element_by_css_selector(".btn-group > a:nth-child(1)")
    assert b_link is not None, "Нет корзины!"

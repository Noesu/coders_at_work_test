from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_coders_at_work(browser):
    browser.get(link)
    time.sleep(3)
    add_btn = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert add_btn.is_enabled(), f'Expected add_to_basket_btn is Enabled, got {add_btn.is_enabled()}'

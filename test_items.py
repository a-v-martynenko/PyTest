import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_pesent(browser):
    browser.get(link)
    time.sleep(30)       

    assert EC.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket")), "Expected: 'Add to basket' button is present. Got: button is missing."
    
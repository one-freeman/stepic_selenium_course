import pytest
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# Ссылка c кнопкой
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# Ссылка без кнопки
link2="http://selenium1py.pythonanywhere.com/"

# Тест проходит когда есть кнопка
def test_find_basket_button(browser):
    try:
        browser.get(link)
        time.sleep(30)
        button=None
        button=browser.find_element(By.CSS_SELECTOR, "button.btn.btn-add-to-basket[type='submit']")        
        print("\n","button.text=", button.text, "\n")    
    except NoSuchElementException:
        assert button is not None, "Кнопка не найдена на странице!"   
        

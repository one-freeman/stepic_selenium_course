from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/wait2.html"
    browser = webdriver.Chrome()

    # говорим WebDriver ждать ВСЕ элементы в течение 5 секунд
    #browser.implicitly_wait(5)
    
    browser.get(link)
    #browser.get("http://suninjuly.github.io/wait2.html")

    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
    button.click()

    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
    

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

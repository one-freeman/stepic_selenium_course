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
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()

    # говорим WebDriver ждать ВСЕ элементы в течение 5 секунд
    #browser.implicitly_wait(5)
    
    browser.get(link)
    #browser.get("http://suninjuly.github.io/wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID,"price"),("$100"))
    )
    button = browser.find_element(By.CSS_SELECTOR, "button.btn#book")
    button.click()

    #message = browser.find_element(By.ID, "verify_message")

    #assert "successful" in message.text


    # Нажать на кнопку
    #button = browser.find_element(By.CSS_SELECTOR, "button.btn#solve")
    #button.click()
    # Confirm
    #confirm = browser.switch_to.alert
    #confirm.accept()
  

    # Извлечь x и посчитать ф-ю
    x_element = browser.find_element(By.CSS_SELECTOR, "label #input_value" )
    x = x_element.text
    y = calc(x)


    # Ввести ответ
    answer = browser.find_element(By.CSS_SELECTOR, "input#answer[required]" )
    answer.send_keys(y)

    time.sleep(1)

    # Подтвердить
    button = browser.find_element(By.CSS_SELECTOR, "button.btn#solve")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    alert = browser.switch_to.alert
    alert_text=alert.text
    print(alert_text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

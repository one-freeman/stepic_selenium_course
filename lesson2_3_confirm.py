from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

# Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
# Confirm
    confirm = browser.switch_to.alert
    confirm.accept()
  

    # Извлечь x и посчитать ф-ю
    x_element = browser.find_element(By.CSS_SELECTOR, "label #input_value" )
    x = x_element.text
    y = calc(x)


    # Ввести ответ
    answer = browser.find_element(By.CSS_SELECTOR, "input#answer[required]" )
    answer.send_keys(y)

    time.sleep(1)

    # Подтвердить
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    alert = browser.switch_to.alert
    alert_text=alert.text
    print(alert_text)
  # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

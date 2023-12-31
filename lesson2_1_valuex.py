from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.CSS_SELECTOR, "img#treasure" )
    x_value = x_element.get_attribute("valuex")
    #x = x_value.text
    x = x_value
    y = calc(x)
    
    answer = browser.find_element(By.CSS_SELECTOR, "input#answer[required]" )
    answer.send_keys(y)
    
       
    # Отправляем заполненную форму
    checkbox = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    radiobutton.click()

    time.sleep(3)
  
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    #time.sleep(3)

    # находим элемент, содержащий текст
    #welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

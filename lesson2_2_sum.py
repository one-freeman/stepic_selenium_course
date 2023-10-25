from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def sum(x,y):
  return str( (int(x))+(int(y)) )

try: 
    link = "http://suninjuly.github.io/selects1.html"
    
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    num1 = browser.find_element(By.CSS_SELECTOR, "span#num1" )
    x=num1.text

    # Ваш код, который заполняет обязательные поля
    num2 = browser.find_element(By.CSS_SELECTOR, "span#num2" )
    y=num1.text
    
    answer=sum(x,y)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(answer) # ищем элемент с текстом "Python"
       
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

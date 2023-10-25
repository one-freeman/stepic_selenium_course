from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.CSS_SELECTOR, "label #input_value" )
    x = x_element.text
    y = calc(x)


    # Прокрутка на кнопку
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Убрать футер
    #    footer = browser.find_element(By.TAG_NAME, "footer")
    #    browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)

    #browser.find_element(By.TAG_NAME,'body').send_keys(Keys.END) #или Home если наверх
    
    answer = browser.find_element(By.CSS_SELECTOR, "input#answer[required]" )
    answer.send_keys(y)
    
       
    # Отправляем заполненную форму
    checkbox = browser.find_element(By.CSS_SELECTOR, "div.form-check-custom [for='robotCheckbox']")
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "div.form-radio-custom [for='robotsRule']")
    radiobutton.click()

    time.sleep(1)
  
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

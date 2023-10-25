from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

#    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname(''))    # получаем путь к директории текущего исполняемого файла 
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

    # Ваш код, который заполняет обязательные поля
    first = browser.find_element(By.CSS_SELECTOR, "input[name='firstname'][required]")
    first.send_keys("Name")
    
    second=browser.find_element(By.CSS_SELECTOR, "input[name='lastname'][required]" )
    flag=second.send_keys("Lastname")
    
    third = browser.find_element(By.CSS_SELECTOR, "input[name='email'][required]" )
    third.send_keys("email@email.ru")

    element = browser.find_element(By.CSS_SELECTOR, "input#file[required]" )
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

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

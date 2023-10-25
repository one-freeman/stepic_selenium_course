import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
link = "http://suninjuly.github.io/registration1.html"

try:
#    executable_path=ChromeDriverManager().install()
#    service=ChromeService(ChromeDriverManager().install())
#    service=ChromeService( ChromeDriverManager(version="114.0.5735.16").install() )
#    options = webdriver.ChromeOptions()
#    browser = webdriver.Chrome(service=service,options=options)
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
    input1.send_keys("name")
    
    input2 = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
    input2.send_keys("surname")
    
    input3 = browser.find_element(By.CSS_SELECTOR, "input.third[required]")
    input3.send_keys("email")


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

    #Открываем страницу
try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #тут код, который делает подсчет из задачи
    x = browser.find_element(By.ID, 'input_value')
    rez = str(math.log(abs(12*math.sin(int(x.text)))))
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(rez)

    #Выбираем чекбокс, радиобаттон и нажимаем сабмит
    box = browser.find_element(By.CSS_SELECTOR, "[class='form-check-input']").click()
    radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
    button = browser.find_element(By.TAG_NAME, "button").click()

    #Закрыть через 10 секунд
finally:
    time.sleep(10)


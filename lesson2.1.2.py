from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


#Открываем страницу
try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Берем значение из картинки
    picture = browser.find_element(By.ID,  "treasure")
    picture_att = picture.get_attribute("valuex")
    rez = str(math.log(abs(12*math.sin(int(picture_att)))))
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(rez)

    #Выбираем чекбокс, радиобаттон и нажимаем сабмит
    box = browser.find_element(By.ID, "robotCheckbox").click()
    radio = browser.find_element(By.ID, "robotsRule").click()
    button = browser.find_element(By.TAG_NAME, "button").click()


    #Закрыть через 10 секунд
finally:
    time.sleep(10)
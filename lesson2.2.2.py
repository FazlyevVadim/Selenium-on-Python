from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

#Открываем ссылку
link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
#Найти Х
x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
rez = str(math.log(abs(12*math.sin(int(x)))))
#Проскролить вниз
browser.execute_script("window.scrollBy(0, 100);")

#Ввести в поле результат Х
answer = browser.find_element(By.ID, 'answer')
answer.send_keys(rez)

#Отметить чекбок,радиобаттон и нажать сабмит
box = browser.find_element(By.CSS_SELECTOR, "[class='form-check-input']").click()
radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
button = browser.find_element(By.TAG_NAME, "button").click()

time.sleep(10)
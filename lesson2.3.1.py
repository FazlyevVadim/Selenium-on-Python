from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


#Открываем ссылку
link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

#Нажимаем кнопку
button = browser.find_element(By.CLASS_NAME,'btn.btn-primary').click()

#Нажимаем на модальное окно
confirm = browser.switch_to.alert
confirm.accept()

#Вычисление формулы
x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
rez = str(math.log(abs(12*math.sin(int(x)))))
answer = browser.find_element(By.ID, 'answer')
answer.send_keys(rez)

#Нажимаем сабмит
button = browser.find_element(By.TAG_NAME, "button").click()

time.sleep(7)
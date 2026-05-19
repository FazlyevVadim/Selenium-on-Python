from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
#Открываем ссылку
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
#Нажимаем на кнопку
button = browser.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary').click()
#Переход на следующее окно
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
#Подсчет формулы
x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
rez = str(math.log(abs(12*math.sin(int(x)))))
answer = browser.find_element(By.ID, 'answer')
answer.send_keys(rez)
#Нажимаем сабмит
button = browser.find_element(By.TAG_NAME, "button").click()
time.sleep(7)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

#Открываем ссылку
link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
#Находим кнопку, которую надо нажать
buttonBook = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
#Пишем ожидание. Оно ничего возвращать не должно. Просто строка кода:
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
#Кликаем по кнопке из п.1
buttonBook.click()
#Прокручиваем страницу вниз
browser.execute_script("window.scrollBy(0, 500);")
#Подсчет формулы
x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
rez = str(math.log(abs(12*math.sin(int(x)))))
answer = browser.find_element(By.ID, 'answer')
answer.send_keys(rez)
#Нажимаем сабмит
button = browser.find_element(By.ID, "solve").click()
time.sleep(7)
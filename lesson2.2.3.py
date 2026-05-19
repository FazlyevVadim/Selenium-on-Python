from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

#Открываем ссылку
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

#Заполнить текстовые поля: имя, фамилия, email
firstName = browser.find_element(By.NAME, 'firstname').send_keys('Иван')
lastName = browser.find_element(By.NAME, 'lastname').send_keys('Петрович')
email = browser.find_element(By.NAME, 'email').send_keys('IvanPetr@mail.ru')

#Работа с файлом
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'newfile')
buttonAddFile = browser.find_element(By.ID, 'file')
buttonAddFile.send_keys(file_path)

#Кнопка сабмит
submit = browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

#Ожидание
time.sleep(7)
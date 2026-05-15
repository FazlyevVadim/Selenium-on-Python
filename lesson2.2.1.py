from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#Открываем ссылку
link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

#Находим 2 числа и считаем их сумму в переменную sum
num_text = browser.find_element(By.ID, "num1").text
num1 = int(num_text)
num_text = browser.find_element(By.ID, "num2").text
num2 = int(num_text)
sum = (num1 + num2)


#Открываем список и находим результат суммы по value
dropdown_element = browser.find_element(By.ID, "dropdown")
select = Select(dropdown_element)
select.select_by_visible_text(str(sum))

#Жмакаем на Сабмит
button = browser.find_element(By.CLASS_NAME, "btn.btn-default").click()

time.sleep(5)


from selenium import webdriver
from selenium.webdriver.common.by import By

#Открываем ссылку
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
#Жмав на кнопку
button = browser.find_element(By.ID, "button")
#Ошибка:NoSuchElementException



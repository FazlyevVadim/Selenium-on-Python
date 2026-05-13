from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

#тут код, который делает подсчет из задачи

box = browser.find_element(By.CSS_SELECTOR, "[class='form-check-input']").click()
radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
button = browser.find_element(By.TAG_NAME, "button").click()

time.sleep(10)


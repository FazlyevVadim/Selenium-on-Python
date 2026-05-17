#Работа со списками
#Списка бывают раскрывающиеся или уже открыте
#Метод который будем использовать: одинаковые, что мы и проходили ранее

#Новый поиск метода select_by_value(value), select.select_by_visible_text("text") и select.select_by_index(index



#from selenium.webdriver.support.ui import Select
#select = Select(browser.find_element(By.TAG_NAME, "select"))
#select.select_by_value("1") # ищем элемент с текстом "Python"


#Метод execute_script
#Зачем это может понадобиться, если в автотестах мы стараемся взаимодействовать с интерфейсом сайта как обычный
#пользователь, нажимая кнопки, выбирая пункты меню и вводя текст в текстовые поля?

from selenium import webdriver
browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")

#Можно с помощью этого метода выполнить сразу несколько инструкций,
#перечислив их через точку с запятой. Изменим сначала заголовок страницы, а затем вызовем alert:
browser.execute_script("document.title='Script executing';alert('Robots at work');")

#"return arguments[0].scrollIntoView(true);"
#браузер дополнительно проскроллит нужный элемент, чтобы он точно стал видимым.
#проскроллить всю страницу целиком на строго заданное количество пикселей. Эта команда проскроллит страницу на 100 пикселей вниз:
#browser.execute_script("window.scrollBy(0, 100);")

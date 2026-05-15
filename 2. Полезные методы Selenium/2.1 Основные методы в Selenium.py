#Checkbox (чекбокс или флажок) и radiobutton (радиобаттон или переключатель) — часто используемые в формах элементы.
#Что бы выбрать чекбокс или радиобаттон пишите click()
#checked - Часто атрибут checked уже установлен для одного из элементов по умолчанию.

#Также вы можете увидеть тег label рядом с input. Этот тег используется, чтобы сделать кликабельным текст,
# который отображается рядом с флажком. Этот текст заключен внутри тега label. Элемент label связывается с элементом
# input с помощью атрибута for, в котором указывается значение атрибута id для элемента input:
# <div>
# <input type="radio" id="python" name="language" checked>
# <label for="python">Python</label>
# </div>


#Задача 1
# ответ в файле lesson2.1.1



#Метод get_attribute
#пример кода
#people_checked = people_radio.get_attribute("checked")
#print("value of people radio: ", people_checked)
#assert people_checked is not None, "People radio is not selected by default"
#пример кода где нет аттрибута чекед
#robots_radio = browser.find_element(By.ID, "robotsRule")
#robots_checked = robots_radio.get_attribute("checked")
#assert robots_checked is None

#Задача 2.1.2
# ответ в файле lesson2.1.2


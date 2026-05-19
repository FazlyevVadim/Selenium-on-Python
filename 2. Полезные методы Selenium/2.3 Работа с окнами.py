#Alerts и как с ними жить (модальное окно)
#alert = browser.switch_to.alert
#alert.accept()

#Чтобы получить текст из alert, используйте свойство text объекта alert:
#alert = browser.switch_to.alert
#alert_text = alert.text

#Другой вариант модального окна, который предлагает пользователю выбор согласиться с сообщением или отказаться от него,
# называется confirm. Для переключения на окно confirm используется та же команда, что и в случае с alert:
#confirm = browser.switch_to.alert
#confirm.accept() или confirm.dismiss()


#Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста. Чтобы ввести текст,
# используйте метод send_keys():
#prompt = browser.switch_to.alert
#prompt.send_keys("My answer")
#prompt.accept()



#Переход на новую вкладку браузера
#browser.switch_to.window(window_name)
#Чтобы узнать имя новой вкладки, нужно использовать метод window_handles
#new_window = browser.window_handles[1]
#first_window = browser.window_handles[0]
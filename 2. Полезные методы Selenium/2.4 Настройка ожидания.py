#Selenium Waits (Implicit Waits)
#жидание при инициализации драйвера, чтобы применить его ко всем тестам.
#browser.implicitly_wait(5)


#Explicit Waits (WebDriverWait и expected_conditions)
#Кнопка может быть неактивной, то есть её нельзя кликнуть;

#Кнопка может содержать текст, который меняется в зависимости от действий пользователя. Например, текст "Отправить"
# после нажатия кнопки поменяется на "Отправлено";

#Кнопка может быть перекрыта каким-то другим элементом или быть невидимой.

#В Selenium WebDriver существует понятие явных ожиданий (Explicit Waits)

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
#button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))

# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
#button = WebDriverWait(browser, 5).until_not(EC.element_to_be_clickable((By.ID, "verify")))
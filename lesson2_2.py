from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    num1 = int(browser.find_element_by_xpath('//*[@id="num1"]').text)
    num2 = int(browser.find_element_by_xpath('//*[@id="num2"]').text)
    sum=num1+num2

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum)) # ищем элемент
    
    button = browser.find_element_by_xpath("/html/body/div[1]/form/button")
    button.click()
#     print('all')

finally:
#     # успеваем скопировать код за 30 секунд
    time.sleep(30)
#     # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
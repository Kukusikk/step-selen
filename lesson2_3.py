from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x=int(browser.find_element_by_xpath('//*[@id="input_value"]').text)

    res=calc(x)

    browser.execute_script('window.scrollBy(0, 100);')  # скролим страницу вниз


    input1 = browser.find_element_by_xpath('//*[@id="answer"]')
    input1.send_keys(res)

    input2 = browser.find_element_by_xpath('//*[@id="robotCheckbox"]')   #простановка чекбокса
    input2.click()

    input3 = browser.find_element_by_xpath('//*[@id="robotsRule"]')    #простановка радиобатон
    input3.click()
    


    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
#     # успеваем скопировать код за 30 секунд
    time.sleep(30)
#     # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
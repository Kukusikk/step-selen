from selenium import webdriver
import time 
import os 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_xpath('/html/body/form/div/div/button')
    button1.click()


    alert = browser.switch_to.alert
    alert.accept()

    x = int(browser.find_element_by_xpath('//*[@id="input_value"]').text)
    res = calc(x)

    input1 = browser.find_element_by_xpath('//*[@id="answer"]') 
    input1.send_keys(str(res)) 
    
    button = browser.find_element_by_xpath("/html/body/form/div/div/button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
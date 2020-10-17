from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element_by_xpath('//*[@id="treasure"]')
    x = x_element.get_attribute('valuex')
    y = calc(x)



    input1 = browser.find_element_by_xpath('//*[@id="answer"]')
    input1.send_keys(y)


    input2 = browser.find_element_by_xpath('//*[@id="robotCheckbox"]')
    input2.click()

    input3 = browser.find_element_by_xpath('//*[@id="robotsRule"]')
    input3.click()
    
    button = browser.find_element_by_xpath("/html/body/div/form/button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
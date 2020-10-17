from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()

    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')  
    )#явно ждем когда цена не станет 100

    button1 = browser.find_element_by_xpath('//*[@id="book"]')
    button1.click()

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
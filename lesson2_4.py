from selenium import webdriver
import time 
import os 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath('/html/body/div[1]/form/div/input[1]')
    input1.send_keys('name')


    input2 = browser.find_element_by_xpath('/html/body/div[1]/form/div/input[2]')
    input2.send_keys('second_name')

    input3 = browser.find_element_by_xpath('/html/body/div[1]/form/div/input[3]')
    input3.send_keys('lada@lada')

    input3 = browser.find_element_by_xpath('//*[@id="file"]') # элимент для загрузки файла

    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, 'file.txt')
    input3.send_keys(file_path)   # передаем ему путь файла который загружеем


    
    button = browser.find_element_by_xpath("/html/body/div[1]/form/button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
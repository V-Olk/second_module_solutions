from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    y = calc(browser.find_element_by_id("input_value").text)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)# Проскроллить страницу вниз До кнопки

    browser.find_element_by_id("answer").send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox").click()

    radiobutton = browser.find_element_by_id("robotsRule").click()

    button.click()

finally:
    time.sleep(10)
    browser.quit()

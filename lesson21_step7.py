from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("treasure").get_attribute("valuex")#получение значения атрибута
    y = calc(x)

    asnwer_el = browser.find_element_by_id("answer").send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox").click()

    radiobutton = browser.find_element_by_id("robotsRule").click()

    #submit_button = browser.find_element_by_class_name("button").click()

finally:
    time.sleep(10)
    browser.quit()

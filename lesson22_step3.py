from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    sum = str(int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text))

    select = Select(browser.find_element_by_id("dropdown")).select_by_value(sum)

finally:
    time.sleep(10)
    browser.quit()

from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    browser.find_element_by_tag_name("button").click()

    y = calc(browser.find_element_by_id("input_value").text)

    browser.find_element_by_id("answer").send_keys(y)

    browser.find_element_by_id("solve").click()

finally:
    time.sleep(10)
    browser.quit()

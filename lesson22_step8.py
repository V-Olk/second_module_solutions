from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_name("firstname").send_keys("Vitalii")
    browser.find_element_by_name("lastname").send_keys("last")
    browser.find_element_by_name("email").send_keys("mail")

    browser.find_element_by_id("file").send_keys(r"C:\Users\Vitaleg\Desktop\0.txt")# загрузка файла

    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(10)
    browser.quit()

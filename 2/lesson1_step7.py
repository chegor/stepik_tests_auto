from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    image = browser.find_element_by_css_selector("img#treasure")
    x = image.get_attribute("valuex")
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    robotcheckbox = browser.find_element_by_id("robotCheckbox")
    robotcheckbox.click()

    robotsrule = browser.find_element_by_id("robotsRule")
    robotsrule.click()

    button = browser.find_element_by_css_selector("button.btn-default")
    button.click()



finally:
    time.sleep(10)
    browser.quit()

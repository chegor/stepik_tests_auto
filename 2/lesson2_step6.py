from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_val = browser.find_element_by_id('input_value')
    x = x_val.text
    result = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(result)
    time.sleep(1)
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    time.sleep(1)

    robotcheckbox = browser.find_element_by_id("robotCheckbox")
    robotcheckbox.click()

    robotrule = browser.find_element_by_id("robotsRule")
    robotrule.click()

    submit = browser.find_element_by_css_selector("button.btn-primary")
    submit.click()





finally:
    time.sleep(10)
    browser.quit()

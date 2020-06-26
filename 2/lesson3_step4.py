from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn-primary")
    button.click()
    time.sleep(2)
    alert = browser.switch_to.alert
    alert.accept()

    full_x = browser.find_element_by_id("input_value")
    x = int(full_x.text)
    result = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(result)

    submit = browser.find_element_by_css_selector("[type='submit'].btn-primary")
    submit.click()


finally:
    time.sleep(7)
    browser.quit()

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    current_window = browser.current_window_handle
    print(current_window)
    button = browser.find_element_by_css_selector("button.trollface")
    button.click()
    current_window = browser.current_window_handle
    print(current_window)


    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    current_window = browser.current_window_handle
    print(current_window)
    print(new_window)

    input = browser.find_element_by_id("input_value")
    x = int(input.text)
    result = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(result)
    submit = browser.find_element_by_css_selector("[type='submit'].btn-primary")
    submit.click()


finally:
    time.sleep(7)
    browser.quit()

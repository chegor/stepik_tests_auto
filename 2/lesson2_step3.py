from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    n1 = browser.find_element_by_id("num1")
    num1 = n1.text
    n2 = browser.find_element_by_id("num2")
    num2 = n2.text
    sum = int(num1) + int(num2)
    print(num1)
    print(num2)
    print(sum)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(str(sum))

    submit = browser.find_element_by_css_selector("button.btn-default")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()

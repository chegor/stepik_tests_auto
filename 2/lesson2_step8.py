from selenium import webdriver
import time
import os


try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_name("firstname")
    name.send_keys("che")

    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("ku")

    mail = browser.find_element_by_name("email")
    mail.send_keys("mail@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')


    file = browser.find_element_by_id("file")
    file.send_keys(file_path)

    submit = browser.find_element_by_css_selector("button.btn-primary")
    submit.click()


finally:
    time.sleep(5)
    browser.quit()

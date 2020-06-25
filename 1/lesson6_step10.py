from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element_by_css_selector(".first_block input.first")
    input_name.send_keys("eygor")
    time.sleep(1)
    input_second = browser.find_element_by_css_selector(".first_block input.second")
    input_second.send_keys("mal")
    time.sleep(1)
    input_mail = browser.find_element_by_css_selector(".first_block input.third")
    input_mail.send_keys("test@gmail.com")
    time.sleep(1)


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(3)

    welcome_text_elt = browser.find_element_by_tag_name("h1")

    welcome_text = welcome_text_elt.text


    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
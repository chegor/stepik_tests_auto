from selenium import webdriver
import time
import unittest


class TestHtml(unittest.TestCase):
    def testPage1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)
        input_name = browser.find_element_by_css_selector(".first_block input.first")
        input_name.send_keys("eygor")
        input_second = browser.find_element_by_css_selector(".first_block input.second")
        input_second.send_keys("mal")
        input_mail = browser.find_element_by_css_selector(".first_block input.third")
        input_mail.send_keys("test@gmail.com")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(1)
        browser.quit()

    def testPage2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)
        input_name = browser.find_element_by_css_selector(".first_block input.first")
        input_name.send_keys("eygor")
        input_second = browser.find_element_by_css_selector(".first_block input.second")
        input_second.send_keys("mal")
        input_mail = browser.find_element_by_css_selector(".first_block input.third")
        input_mail.send_keys("test@gmail.com")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(1)
        browser.quit()

if __name__ == "__main__":
    unittest.main()
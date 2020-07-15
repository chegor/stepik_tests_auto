import pytest
from selenium import webdriver
import time
import math

final = ''

list_of_urls = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(7)
    yield browser
    print("\nquit browser..")
    browser.quit()
    #print(final)


@pytest.mark.parametrize('url', list_of_urls)
class TestUrls:
    def test_found_errors(self, browser, url):
        answer = math.log(int(time.time()))
        browser.get(url)
        input_area = browser.find_element_by_css_selector('.textarea')
        input_area.send_keys(str(answer))
        button = browser.find_element_by_css_selector('button.submit-submission')
        button.click()
        feedback = browser.find_element_by_css_selector('.smart-hints__hint')
        feedback_text = feedback.text
        try:
            assert feedback_text == 'Correct!', "WRONG TEXT: " + feedback_text
        except AssertionError:
            final += feedback_text
            #To print final - change scope in fixture to "session" and uncomment print


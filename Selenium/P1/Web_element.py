from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver= webdriver.Chrome()
        self.driver.get('https://sahitest.com/demo/linkTest.htm')

    def test_webelement_prop(self):
        self.driver.find_element(By.ID,value='t1')

    def test_web_element(self):
        e=self.driver.find_element(By.ID,value='t1')
        e.send_keys('hello')
        sleep(2)


        print(e.get_attribute('type'))
        print(e.get_attribute('name'))
        print(e.get_attribute('value'))
        print(e.value_of_css_property('font'))
        sleep(2)
        e.clear()

if __name__== '__main__':
    case = TestCase()
    # case.test_id()
    case.test_web_element()
from webdriver_helper import get_webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

# driver= get_webdriver() #Get broswer driver

# driver.get('https://baidu.com')


# driver.find_element(by='xpath',value='//*[@id="kw"]').send_keys('selenium')

# driver.find_element(By.CSS_SELECTOR, value='#su').click()
class TestCase(object):
    def __init__(self):
        self.driver=webdriver.Chrome()

    def test(self):
        self.driver.get('https://baidu.com')
        self.driver.find_element(by='xpath',value='//*[@id="kw"]').send_keys('selenium')
        self.driver.find_element(By.CSS_SELECTOR, value='#su').click()
        sleep(3)
        self.driver.quit()


if __name__== '__main__':
    case = TestCase()
    case.test()
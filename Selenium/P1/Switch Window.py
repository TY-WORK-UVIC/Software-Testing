from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver= webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
 
        sleep(1)
    def test_prop(self):
        print(self.driver.name)
        print(self.driver.current_url)
        print(self.driver.title)
        print(self.driver.window_handles)
        sleep(1)
    def test_method(self):
        self.driver.find_element(By.CLASS_NAME, value='s_ipt').send_keys('selenium')
        self.driver.find_element(By.CSS_SELECTOR, value='#su').click()
        sleep(2)
        self.driver.back()
        sleep(1)
        self.driver.forward()
        sleep(2)

    def test_window(self):
        self.driver.find_element(By.LINK_TEXT,value='新闻').click()
        windows=self.driver.window_handles

        while 1:
            for window in windows:
                self.driver.switch_to.window(window)
                sleep(2)


if __name__== '__main__':
    case = TestCase()
    # case.test_id()
    case.test_window()
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver= webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
        sleep(1)

    def test_id(self):
                
        self.driver.find_element(by='id',value='kw').send_keys('selenium')
        self.driver.find_element(By.CSS_SELECTOR, value='#su').click()
        sleep(3)
        # self.driver.quit()
    def test_name(self):
        self.driver.find_element(by='name', value='wd').send_keys('selenium')
        self.driver.find_element(By.CSS_SELECTOR, value='#su').click()
        sleep(3)
        self.driver.quit()

    def test_linktext(self):
        self.test_id()
        self.driver.find_element(By.LINK_TEXT,value='百度首页').click()
   
        sleep(3)
     
    def test_partial_link_test(self):
        self.test_id()
        self.driver.find_element(By.PARTIAL_LINK_TEXT ,value='首页').click()
   
        sleep(3)
    def test_xpath(self):
        self.driver.find_element(By.XPATH ,value='//*[@id="kw"]').send_keys('selenium')
        self.driver.find_element(By.CSS_SELECTOR, value='#su').click()
        sleep(3)
    def test_tag(self):
        self.driver.find_element(By.TAG_NAME, value='input')
        print(input)
    
    def test_css_selector(self):
        self.driver.find_element(By.CSS_SELECTOR ,value='#kw').send_keys('selenium')
        self.driver.find_element(By.CSS_SELECTOR, value='#su').click()
        sleep(3)
    def test_class(self):
        self.driver.find_element(By.CLASS_NAME, value='s_ipt').send_keys('selenium')
        self.driver.find_element(By.CSS_SELECTOR, value='#su').click()
        sleep(3)



if __name__== '__main__':
    case = TestCase()
    # case.test_id()
    case.test_class()
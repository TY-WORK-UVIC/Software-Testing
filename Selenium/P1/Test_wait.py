from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestCase(object):
    def __init__(self):
        self.driver= webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')

    def test_sleep(self):
        self.driver.find_element(By.ID, value='kw').send_keys('selenium')
        sleep(2)
        self.driver.find_element(By.ID, value='su').click()
        sleep(3)
    
    def test_implicity(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, value='kw').send_keys('selenium')
       
        self.driver.find_element(By.ID, value='su').click()

    def test_wait(self):
        wait= WebDriverWait(self.driver,2)
        wait.until(EC.title_is('百度一下，你就知道'))
        self.driver.find_element(By.ID, value='kw').send_keys('selenium')
       
        self.driver.find_element(By.ID, value='su').click()




if __name__== '__main__':
    case = TestCase()
    case.test_wait()
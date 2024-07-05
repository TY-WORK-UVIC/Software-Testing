from time import sleep,strftime,localtime, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
class TestCase(object):
    def __init__(self):
        self.driver= webdriver.Chrome()
        self.driver.get('https://sahitest.com/demo/framesTest.htm')

    def test(self):
        
        top=self.driver.find_element(By.NAME,value='top')
        self.driver.switch_to.frame(top)
        self.driver.find_element(By.XPATH, value='/html/body/table/tbody/tr/td[1]/a[1]').click()

        

        self.driver.switch_to.default_content()
        sleep(3)
        second=self.driver.find_element(By.XPATH, value='/html/frameset/frame[2]')

        self.driver.switch_to.frame(second)
        self.driver.find_element(By.XPATH, value='/html/body/table/tbody/tr/td[1]/a[2]').click()
        sleep(3)

if __name__== '__main__':
    case = TestCase()
    case.test()
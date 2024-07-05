from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains
class TestCase(object):
    def __init__(self):
        self.driver= webdriver.Chrome()
        #self.driver.get('https://sahitest.com/demo/clicks.htm')
    def test_mouth(self):
        
        btn=self.driver.find_element(By.XPATH,value='/html/body/form/input[2]')
        ActionChains(self.driver).double_click(btn).perform()

        sleep(2)

        btn1=self.driver.find_element(By.XPATH,value='/html/body/form/input[3]')
        ActionChains(self.driver).click(btn1).perform()

        sleep(2)

        btn2=self.driver.find_element(By.XPATH,value='/html/body/form/input[4]')
        ActionChains(self.driver).context_click(btn2).perform()

        sleep(5)
    def test_key(self):
        
        kw=self.driver.find_element(By.ID,value='kw')
        kw.send_keys('selenium')
        kw.send_keys(Keys.CONTROL,'a')

        sleep(2)

        kw.send_keys(Keys.CONTROL,'x')

        sleep(2)
        kw.send_keys(Keys.CONTROL,'v')
        sleep(2)

        
        
        sleep(2)
        
    def test_move(self):
        self.driver.get('https://www.google.ca/')
        e=self.driver.find_element(By.XPATH,value='/html/body/div[1]/div[1]/a[1]')
        ActionChains(self.driver).move_to_element(e).click(e).perform()
        sleep(2)
        




if __name__== '__main__':
    case = TestCase()
    case.test_move()
    
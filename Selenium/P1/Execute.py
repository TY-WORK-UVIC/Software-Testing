from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestCase(object):
    def __init__(self):
        self.driver= webdriver.Chrome()
        self.driver.get('https://www.google.ca/')


    def test1(self):
        self.driver.execute_script("alert('test')")
        sleep(2)
        self.driver.switch_to.alert.accept()
    def test2(self):
        js='return document.title'
        title=self.driver.execute_script(js)
        print(title)
    def test3(self):
        js="var q= document.getElementById('APjFqb'); q.style.border='2px solid red'"
        self.driver.execute_script(js)

    def test4(self):
        self.driver.find_element(By.ID,value='APjFqb').send_keys('selenium')
        
        self.driver.find_element(By.XPATH,value='//*[@aria-label="Google Search"]').click()
        sleep(2)
        js= 'window.scrollTo(0,document.body.scrollHeight)'
        self.driver.execute_script(js)
        sleep(2)
if __name__== '__main__':
    case = TestCase()
    case.test4()
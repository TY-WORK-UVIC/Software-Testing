from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import os 


class TestCase(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        path= os.path.dirname(os.path.abspath(__file__))
        file_path=path+'/From.html'
        print(path)
        self.driver.get(file_path)
     
    def test_login(self):
        username= self.driver.find_element(By.ID, value='username')
        username.send_keys('admin')
        pwd=self.driver.find_element(By.ID, value='pwd')
        pwd.send_keys('123')

        print(username.get_attribute('value'))
        print(pwd.get_attribute('value'))
        sleep(2)
        self.driver.find_element(By.ID, value='submit').click()
        username.clear()
        pwd.clear()
        sleep(2)

    
if __name__== '__main__':
    case = TestCase()
    case.test_login()

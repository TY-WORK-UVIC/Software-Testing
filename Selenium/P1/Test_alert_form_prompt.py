
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os 
class TestCase(object):
    def __init__(self):
        self.driver= webdriver.Chrome()
        path= os.path.dirname(os.path.abspath(__file__))
        file_path=path+'/Test_Alert.html'
        print(path)
        self.driver.get(file_path)
        sleep(2)

    def test_alert(self):
        self.driver.find_element(By.ID, value='alert').click()
        alert= self.driver.switch_to.alert
        print(alert.text)
        sleep(3)
        alert.accept()
        sleep(3)

    def test_confirm(self):
        self.driver.find_element(By.ID, value='confirm').click()
        confirm= self.driver.switch_to.alert
        print(confirm.text)
        sleep(3)
        confirm.dismiss()
        sleep(3)

    def test_prompt(self):
        self.driver.find_element(By.ID, value='prompt').click()
        prompt= self.driver.switch_to.alert
        print(prompt.text)
        sleep(3)
        prompt.accept()
        sleep(3)






if __name__== '__main__':
    case = TestCase()
    case.test_prompt()
    
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCase(object):
    def __init__(self):
        self.driver= webdriver.Chrome()
        path= os.path.dirname(os.path.abspath(__file__))
        file_path=path+'/Wait.html'
        print(path)
        self.driver.get(file_path)
    def test(self):
        self.driver.find_element(By.ID, value='btn').click()
        wait=WebDriverWait(self.driver,3)

        wait.until(EC.text_to_be_present_in_element((By.ID,'id2'),'id2'))
        print('ok')

if __name__== '__main__':
    case = TestCase()
    case.test()
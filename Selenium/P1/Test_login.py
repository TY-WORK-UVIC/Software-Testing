from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
class TestCase(object):
    def __init__(self):
        self.driver= webdriver.Chrome()
        path= os.path.dirname(os.path.abspath(__file__))
        file_path=path+'/Forms.html'
        print(path)
        self.driver.get(file_path)
    
    
    def test_check_box(self):
        swimming=self.driver.find_element(By.NAME, value='swiming')
        if not swimming.is_selected():
            swimming.click()

        reading= self.driver.find_element(By.NAME, value='reading')
        if not reading.is_selected():
            reading.click()
        sleep(5)
        swimming.click()
        reading.click()
        sleep(3)

    def test_radio(self):
        lst= self.driver.find_elements(By.NAME, value='gender')
        lst[0].click()
        sleep(3)


if __name__== '__main__':
    case = TestCase()
    case.test_radio()
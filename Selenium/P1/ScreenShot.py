from time import sleep,strftime,localtime, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
class TestCase(object):
    def __init__(self):
        self.driver= webdriver.Chrome()
        self.driver.get('https://www.google.ca/')

    def test1(self):
        input=self.driver.find_element(By.CLASS_NAME, value='gLFyf')
        input.send_keys('selenium'+Keys.ENTER)
        sleep(2)

        st=strftime("%Y-%m-%d-%H-%M-%S",localtime(time()))
        file_name=st+'.png'
        self.driver.save_screenshot(file_name)
        path= os.path.abspath('ScreenShot')
        file_path=path+'/'+file_name
        self.driver.get_screenshot_as_file(file_path)


if __name__== '__main__':
    case = TestCase()
    case.test1()

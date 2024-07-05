from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os 
class TestCase(object):
    def __init__(self):
        self.driver= webdriver.Chrome()
        path= os.path.dirname(os.path.abspath(__file__))
        file_path=path+'/Forms2.html'
        print(path)
        self.driver.get(file_path)
   
    def test_select(self):
        se=self.driver.find_element(By.ID, value='province')
        select=Select(se)

        for option in select.options:
            print(option.text)
            

        # for i in range(3):
        #     select.select_by_index(i)
        #     sleep(1)
        # sleep(2)

        # select.deselect_all()
        # sleep(2)
        # select.select_by_index(2)
        # sleep(2)

        # select.select_by_value('bj')
        # sleep(2)

        # select.select_by_visible_text('Tianjing')
        # sleep(2)


if __name__== '__main__':
    case = TestCase()
    case.test_select()
    
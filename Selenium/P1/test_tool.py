
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_element(driver,*loc):

    e=driver.find_element(*loc)
    return e

if __name__ == '__main__':
    driver= webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    location= (By.ID,'kw')
    location2= (By.ID,'su')
    get_element(driver,*location).send_keys('selenium')
    get_element(driver,*location2).click()
    sleep(3)

    
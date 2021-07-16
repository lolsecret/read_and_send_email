import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
email = 'lucallonso@gmail.com'
def find_and_send(name, text):
    elem = driver.find_element_by_name(name)
    elem.clear()
    return elem.send_keys(text)

def send_button(name):
    driver.implicitly_wait(10)
    button = driver.find_element_by_class_name(name)
    return button.click()

driver.get("https://mail.ktga.kz")
elem1 = find_and_send('username', 'k.amanova@ktga.kz')
elem2 = find_and_send('password', 'K.,k.;bpym999')
enter = send_button('signinTxt')

""" IN EMAIL"""
time.sleep(5)
find_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div[5]/div/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/button/span[2]')
find_button.click()
find_button.send_keys(Keys.ENTER)
driver.close()
# find_button.click()

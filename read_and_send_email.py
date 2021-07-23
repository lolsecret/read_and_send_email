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
find_button = driver.find_element_by_xpath(
    '//*[@title="BotagozZTU@halykbank.kz"]').click()
# find_button.click()

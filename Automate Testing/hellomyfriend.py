import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://172.26.3.11:8080/jw/web/login')

driver.implicitly_wait(10)

username = driver.find_element(By.ID, 'j_username')
password = driver.find_element(By.ID, 'j_password')
Login = driver.find_element(By.NAME, 'submit')


username.send_keys('dusit.bua')
password.send_keys('dusit.bua')
Login.click()

driver.implicitly_wait(10)

input('Press ANY KEY to continue...')
driver.quit()
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome() 

driver.get('http://172.26.3.11:8080/jw/web/login') #getเว็บไซต์

driver.implicitly_wait(10)

username = driver.find_element(By.ID, 'j_username')
password = driver.find_element(By.ID, 'j_password')
login = driver.find_element(By.NAME, 'submit')

username.send_keys('dusit.bua') # กรอก username
password.send_keys('dusit.bua') # กรอก password
login.click()

driver.implicitly_wait(10)

driver.get('http://172.26.3.11:8080/jw/web/userview/HRM_Recruitment/v/_/Welcome')

input('Press Enter to continue...')
driver.quit()
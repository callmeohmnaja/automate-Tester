import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from colorama import Fore, Style, init

init(autoreset=True)

driver = webdriver.Chrome()

driver.get('http://172.26.3.11:8080/jw/web/login')

username = driver.find_element(By.ID, 'j_username')
password = driver.find_element(By.ID, 'j_password')
Login = driver.find_element(By.NAME, 'submit')

username.send_keys('dusit.bua')
password.send_keys('dusit.bua')
Login.click()

driver.get('http://172.26.3.11:8080/jw/web/userview/HRM_Recruitment/v/_/Welcome')
driver.get('http://172.26.3.11:8080/jw/web/userview/HRM_Recruitment/v/_/5B4BCB9413D64BF0ACABA4F66F302079?_action=assignmentView&activityId=7233599_50470_HRM_Recruitment_process64_activity1')

add = driver.find_element(By.CLASS_NAME, 'grid-action-add')
add.click()

input("ป้อนค่าเพื่อจบการทํางาน")
driver.quit()
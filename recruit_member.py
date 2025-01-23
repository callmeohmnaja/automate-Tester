from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome() # เปิด Chrome driver

try:
   
    driver.get("http://172.26.3.11:8080/jw/web/login")

    Username = driver.find_element(By.ID, 'j_username')
    password = driver.find_element(By.ID, 'j_password')
    login = driver.find_element(By.NAME, 'submit')

    Username.send_keys("dusit.bua")
    password.send_keys("dusit.bua")
    login.click()

    
    driver.implicitly_wait(10) #load


    driver.get("http://172.26.3.11:8080/jw/web/userview/HRM_Recruitment/v/_/Welcome") #เปิดหน้าสรรหาพนักงาน
    driver.implicitly_wait(10)


    driver.get("http://172.26.3.11:8080/jw/web/userview/HRM_Recruitment/v/_/5B4BCB9413D64BF0ACABA4F66F302079?_action=assignmentView&activityId=7227407_49404_HRM_Recruitment_process64_activity1")

    
    add_button = driver.find_element(By.CLASS_NAME, 'grid-action-add')
    add_button.click()
   
    driver.implicitly_wait(10)

    
finally:
    input("กดปุ่ม Enter เพื่อจบการทำงาน...")
    driver.quit()


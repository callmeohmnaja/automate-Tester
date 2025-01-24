import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome()

try:
 
    driver.get("http://172.26.3.11:8080/jw/web/login")

    
    username = driver.find_element(By.ID, 'j_username')
    password = driver.find_element(By.ID, 'j_password')
    login = driver.find_element(By.NAME, 'submit')

    username.send_keys("dusit.bua")
    password.send_keys("dusit.bua")
    login.click()

  
    driver.implicitly_wait(10)

    
    if "้home" in driver.current_url:
        print("Login Fail")
    else:
        print("Login Success")

   
    driver.get("http://172.26.3.11:8080/jw/web/userview/gd_SelfService/gdSelfService/_/welcome")
    driver.implicitly_wait(10)


    driver.get("http://172.26.3.11:8080/jw/web/userview/gd_SelfService/leaveRequest/_/welcome")
    driver.implicitly_wait(10)

  
    driver.get("http://172.26.3.11:8080/jw/web/userview/gd_SelfService/leaveRequest/_/frmLeave_submit?_action=assignmentView&activityId=7227726_49478_gd_SelfService_process8_newLAform")
    driver.implicitly_wait(10)

    #dropdown ="ลาป่วย"
    leave_type_dropdown = driver.find_element(By.NAME, 'LeaveType')
    select = Select(leave_type_dropdown)
    select.select_by_value("01")  # เลือก "ลาป่วย" (value="01")

    print("เลือกประเภทการลา: ลาป่วย สำเร็จ")

    why = driver.find_element(By.ID, 'dueTo')
    why.send_keys("เป็นไข้")

    input("กด Enter เพื่อออก")

finally:
  
    driver.quit()

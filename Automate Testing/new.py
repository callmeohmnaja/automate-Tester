from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

try:    
    driver.get("http://172.26.3.11:8080/jw/web/login")

    username = driver.find_element(By.ID, 'j_username')
    password = driver.find_element(By.ID, 'j_password')
    login = driver.find_element(By.NAME, 'submit')
    print('เปิดหน้าเว็บ Login')

    username.send_keys("dusit.bua") #ใช้ชื่อผู้ใช้เข้าสู่ระบบ
    password.send_keys("dusit.bua") #pass
    login.click()
    print('เข้าสู่ระบบสําเร็จ')

    driver.get('http://172.26.3.11:8080/jw/web/userview/gd_SelfService/gdSelfService/_/welcome')
    print('เข้าสู่หน้าบริการด้วยตัวเองสําเร็จ')
    driver.implicitly_wait(10)

    driver.get('http://172.26.3.11:8080/jw/web/userview/gd_SelfService/leaveRequest/_/welcome')
    print('เข้าสู่หน้าการลาสําเร็จ')
    driver.implicitly_wait(10)

    driver.get('http://172.26.3.11:8080/jw/web/userview/gd_SelfService/leaveRequest/_/frmLeave_submit?_action=assignmentView&activityId=7232742_50358_gd_SelfService_process8_newLAform')
    driver.implicitly_wait(10)

    Type = driver.find_element(By.NAME, 'LeaveType')
    select = Select(Type)
    select.select_by_value("01")  # ลาป่วย
    print('เลือกประเภทการลา: ลาป่วย สําเร็จ')

    why = driver.find_element(By.ID, 'dueTo')
    why.send_keys("ทดสอบเป็นไข้")

    driver.implicitly_wait(10)

    contact = driver.find_element(By.ID, 'contact')
    contact.send_keys("086-123-4567")

finally:
    input("กดปุ่ม Enter เพื่อจบการทำงาน...")
    driver.quit()
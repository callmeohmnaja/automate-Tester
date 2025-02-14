import time
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# เปิด WebDriver
driver = webdriver.Chrome()
try:
    driver.get("http://172.26.3.11:8080/jw/web/login")

    username = driver.find_element(By.ID, 'j_username')
    password = driver.find_element(By.ID, 'j_password')
    login = driver.find_element(By.NAME, 'submit')
    print("เปิดหน้าเว็บ Login สำเร็จ")

    username.send_keys("dusit.bua")
    password.send_keys("dusit.bua")
    login.click()
    print("กรอกข้อมูล Login สำเร็จ")

    # ไปยังหน้ารายการรออนุมัติ
    driver.get('http://172.26.3.11:8080/jw/web/userview/HRM_Recruitment/v/_/BD4B0A65A1AB49CCAFBB3877FAA13F5E')
    print("ไปยังหน้ารายการรออนุมัติ สำเร็จ")

    # ไปยังหน้าแบบฟอร์มที่ต้องการอนุมัติ
    driver.get("http://172.26.3.11:8080/jw/web/userview/HRM_Recruitment/v/_/9987B5EE6FE34CC6BD68198F1F638C50?activityId=7233136_50376_HRM_Recruitment_process64_activity10&_mode=assignment")
    print("ไปยังหน้ารายการรออนุมัติแบบฟอร์ม สำเร็จ")

    # รอให้ radio button ปรากฏขึ้น
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='approvedStatus' and @value='Approved']"))
    )

    # เลือก radio button 'Approved'
    approved_radio = driver.find_element(By.XPATH, "//input[@name='approvedStatus' and @value='Approved']")
    driver.execute_script("arguments[0].click();", approved_radio)
    print("เลือกสถานะ 'Approved' สำเร็จ")

    # คลิกปุ่ม Complete
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'assignmentComplete'))
    ).click()
    print("คลิกปุ่ม Complete สำเร็จ")

finally:
    input("กดปุ่ม Enter เพื่อจบการทำงาน...")
    driver.quit()

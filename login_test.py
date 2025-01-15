from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()  # เปิด Chrome driver

test_results = []  # เก็บผลลัพธ์การทดสอบ

def check_login_status(expected_success, test_case_name):
    """
    ตรวจสอบสถานะการเข้าสู่ระบบ
    - expected_success: True หากคาดว่าจะเข้าสู่ระบบสำเร็จ, False หากคาดว่าจะล้มเหลว
    - test_case_name: ชื่อกรณีทดสอบ
    """
    try:
        if expected_success:
            # ตรวจสอบองค์ประกอบเฉพาะของหน้าเว็บหลังเข้าสู่ระบบ เช่น dropdown-menu
            driver.find_element(By.CLASS_NAME, "dropdown-menu")
            print(f"\033[1;32m✅ สำเร็จ: {test_case_name} ได้สำเร็จ\033[0m")
            test_results.append((test_case_name, "สำเร็จ"))
        else:
            # ตรวจสอบว่าหน้าเว็บยังคงแสดงฟิลด์ username/password (แปลว่าล้มเหลว)
            driver.find_element(By.ID, "j_username")
            print(f"\033[1;32m✅ สำเร็จ: {test_case_name} ล้มเหลวตามที่คาดไว้\033[0m")
            test_results.append((test_case_name, "สำเร็จ"))
    except NoSuchElementException:
        if expected_success:
            print(f"\033[1;31m❌ ล้มเหลว: {test_case_name} ไม่สำเร็จตามที่คาดไว้\033[0m")
            test_results.append((test_case_name, "ล้มเหลว"))
        else:
            print(f"\033[1;31m❌ ล้มเหลว: {test_case_name} ไม่ล้มเหลวตามที่คาดไว้\033[0m")
            test_results.append((test_case_name, "ล้มเหลว"))

try:
    # กรณีที่ 1: ใส่ username และ password ถูกต้อง
    test_case_name = "กรณีที่ 1: Login ด้วยรหัสผ่านที่ถูกต้อง"
    print(f"\n\033[1;33mเริ่มการทดสอบ {test_case_name}...\033[0m")
    driver.get("http://172.26.3.11:8080/jw/web/login")
    
    username_field = driver.find_element(By.ID, "j_username")
    password_field = driver.find_element(By.ID, "j_password")
    login_button = driver.find_element(By.NAME, "submit")
    
    username_field.send_keys("wientian.kod")
    password_field.send_keys("wientian.kod")
    login_button.click()
    
    print("\033[1;36m🔄 กำลังตรวจสอบสถานะการเข้าสู่ระบบ...\033[0m")
    check_login_status(expected_success=True, test_case_name=test_case_name)

    # กรณีที่ 2: ใส่ username ถูกต้อง แต่ password ผิด
    test_case_name = "กรณีที่ 2: Login ด้วยรหัสผ่านที่ผิด"
    print(f"\n\033[1;33mเริ่มการทดสอบ {test_case_name}...\033[0m")
    driver.get("http://172.26.3.11:8080/jw/web/login")
    
    username_field = driver.find_element(By.ID, "j_username")
    password_field = driver.find_element(By.ID, "j_password")
    login_button = driver.find_element(By.NAME, "submit")
    
    username_field.send_keys("panida.oun")
    password_field.send_keys("wrong_password")
    login_button.click()
    
    print("\033[1;36m🔄 กำลังตรวจสอบสถานะการเข้าสู่ระบบ...\033[0m")
    check_login_status(expected_success=False, test_case_name=test_case_name)

finally:
    print("\033[1;34mสิ้นสุดการทดสอบ! ปิด Browser...\033[0m")
    driver.close()

    # สรุปผลการทดสอบ
    print("\n\033[1;33m=== สรุปผลการทดสอบ ===\033[0m")
    for test_case, result in test_results:
        print(f"{test_case}: {result}")

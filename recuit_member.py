from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# เริ่มต้น WebDriver
driver = webdriver.Chrome()

try:
    # Test Case: เข้าสู่ระบบและเปิดหน้าแบบฟอร์มขอสรรหา
    test_case_name = 'กรณีที่ 2: เชื่อมต่อไปยังหน้าแบบฟอร์มขอสรรหา'
    print(f"\n\033[1;33mเริ่มการทดสอบ {test_case_name}...\033[0m")
    
    # เปิดหน้าเข้าสู่ระบบ
    driver.get("http://172.26.3.11:8080/jw/web/login")
    
    # เข้าสู่ระบบ
    username = driver.find_element(By.ID, 'j_username')
    password = driver.find_element(By.ID, 'j_password')
    login_button = driver.find_element(By.NAME, 'submit')
    
    username.send_keys("panida.oun")
    password.send_keys("panida.oun")
    login_button.click()
    
    # รอให้ลิงก์ "สรรหา-คัดเลือก" ปรากฏ
    wait = WebDriverWait(driver, 10)
    recruitment_link = wait.until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "สรรหา-คัดเลือก"))
    )
    
    # คลิกลิงก์ "สรรหา-คัดเลือก"
    recruitment_link.click()
    print("\033[1;32mเข้าสู่หน้าระบบสรรหา-คัดเลือกสำเร็จ!\033[0m")
    
    # รอให้ลิงก์หรือปุ่มแบบฟอร์มขอสรรหา (<i class="fa fa-file-text"></i>) ปรากฏ
    form_icon = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "i.fa.fa-file-text"))
    )
    
    # คลิกที่ไอคอนแบบฟอร์มขอสรรหา
    form_icon.click()
    print("\033[1;32mเข้าสู่หน้าแบบฟอร์มขอสรรหาได้สำเร็จ!\033[0m")
    
except TimeoutException:
    print("\033[1;31mทดสอบล้มเหลว: ไม่พบองค์ประกอบที่กำหนดภายในเวลาที่กำหนด.\033[0m")
except NoSuchElementException as e:
    print(f"\033[1;31mทดสอบล้มเหลว: {e}\033[0m")
finally:
    input("กด Enter เพื่อปิดเบราว์เซอร์...")
    driver.quit()

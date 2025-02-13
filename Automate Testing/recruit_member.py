from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()

try:
    driver.get("http://172.26.3.11:8080/jw/web/login")
    driver.maximize_window()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'j_username'))).send_keys("dusit.bua")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'j_password'))).send_keys("dusit.bua")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'submit'))).click()
    print("เข้าสู่ระบบสำเร็จ")

    driver.implicitly_wait(10)
    driver.get("http://172.26.3.11:8080/jw/web/userview/HRM_Recruitment/v/_/Welcome")
    driver.get("http://172.26.3.11:8080/jw/web/userview/HRM_Recruitment/v/_/5B4BCB9413D64BF0ACABA4F66F302079?_action=assignmentView&activityId=7227407_49404_HRM_Recruitment_process64_activity1")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'grid-action-add'))).click()
    print("คลิกปุ่ม Add สำเร็จ")

    try:
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "iframe"))
        )
        driver.switch_to.frame(iframe)
        print("สลับไปยัง iframe สำเร็จ")
    except Exception as e:
        print(f"ไม่พบ iframe: {e}")

    try:
        radio_button = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='methodRecruit' and @value='1']"))
        )
        print("พบ radio button ใน DOM")
    except Exception as e:
        print(f"ไม่พบ radio button ใน DOM: {e}")
        raise

    driver.execute_script("arguments[0].checked = true;", radio_button)
    driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", radio_button)
    print("เลือก radio button ด้วย JavaScript สำเร็จ")

except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")

finally:
    input("กดปุ่ม Enter เพื่อจบการทำงาน...")
    driver.quit()
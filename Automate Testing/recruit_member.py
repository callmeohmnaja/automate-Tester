from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import init, Fore

#ระบบสรรหาพนักง๊าน = 1,2,3
#1 = สรรหาพนักงานจากภายนอก
#2 = สรรหาพนักงานจากภายใน
#3 = สรรหาพนักงานจากภายนอกและภายใน

init(autoreset=True)  # เปิดใช้งาน colorama

driver = webdriver.Chrome()

try: 
    driver.get('http://172.26.3.11:8080/jw/web/login') #getเว็บไซต์

    username = driver.find_element(By.ID, 'j_username')
    password = driver.find_element(By.ID, 'j_password')
    login = driver.find_element(By.NAME, 'submit')

    username.send_keys('dusit.bua') # กรอก username
    password.send_keys('dusit.bua') # กรอก password
    login.click()

    driver.implicitly_wait(10)
    driver.get('http://172.26.3.11:8080/jw/web/userview/appcenter/JogetGistda/_/home')
    driver.get('http://172.26.3.11:8080/jw/web/userview/HRM_Recruitment/v/_/5B4BCB9413D64BF0ACABA4F66F302079?_action=assignmentView&activityId=7233129_50409_HRM_Recruitment_process64_activity1')

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'grid-action-add'))).click()
    print(Fore.GREEN + "✅ คลิกปุ่ม Add สำเร็จ")

    try:
        iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        driver.switch_to.frame(iframe)
        print(Fore.GREEN + "✅ สลับไปยัง iframe สำเร็จ")
    except Exception:
        print(Fore.YELLOW + "⚠️ ไม่พบ iframe หรือไม่จำเป็นต้องสลับ")

    try:
        radio_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='methodRecruit' and @value='1']")) #ป้อนคค่าใดค่าหนึ่ง {1,2,3}
        )
        driver.execute_script("arguments[0].checked = true;", radio_button)
        driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", radio_button)
        print(Fore.GREEN + "✅ เลือก radio button สำเร็จ")
    except Exception as e:
        print(Fore.RED + f"❌ ไม่พบ radio button: {e}")

    try:
        requestAge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'requestAge')))
        requestAge.send_keys("23")
        print(Fore.GREEN + "✅ กรอกอายุขั้นต่ำสำเร็จ")
    except Exception as e:
        print(Fore.RED + f"❌ ไม่พบช่องกรอกอายุขั้นต่ำ: {e}")

    try:
        requestAgeEnd = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'requestAgeEnd')))
        driver.execute_script("arguments[0].value = '49';", requestAgeEnd)
        driver.execute_script("arguments[0].dispatchEvent(new Event('input'));", requestAgeEnd)
        print(Fore.GREEN + "✅ กรอกอายุสูงสุดสำเร็จ")
    except Exception as e:
        print(Fore.RED + f"❌ ไม่พบช่องกรอกอายุสูงสุด: {e}")

    try:
        requestRemark = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'requestRemark')))
        requestRemark.send_keys("ทดสอบการเพิ่มเงื่อนไขการรับสมัครพนักงาน")
        print(Fore.GREEN + "✅ กรอกข้อความเพิ่มเติมสำเร็จ")
    except Exception as e:
        print(Fore.RED + f"❌ ไม่พบช่องกรอกข้อความเพิ่มเติม: {e}")

except Exception as e:
    print(Fore.RED + f"❌ เกิดข้อผิดพลาด: {e}")

try:
    requestValue = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'requestValue')))

    if requestValue.is_displayed():
        requestValue.clear()
        requestValue.send_keys("50000")
        print(Fore.GREEN + "✅ กรอกเงินเดือนสำเร็จ")
    else:
        print(Fore.YELLOW + "⚠️ ช่องกรอกเงินเดือนถูกซ่อนอยู่ ไม่สามารถใส่ค่าได้")

except Exception as e:
    print(Fore.RED + f"❌ ไม่พบช่องกรอกเงินเดือน: {e}")

try:
    requestJD = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'requestJD')))

    if requestJD.is_displayed():
        requestJD.clear()
        requestJD.send_keys("ทดสอบกรอกรายละเอียดงาน")
        print(Fore.GREEN + "✅ กรอกรายละเอียดงานสำเร็จ")
    else:
        print(Fore.YELLOW + "⚠️ ช่องกรอกรายละเอียดถูกซ่อนอยู่ ไม่สามารถใส่ค่าได้")

except Exception as e:
    print(Fore.RED + f"❌ ไม่พบช่องกรอกรายละเอียดงาน: {e}")

try:
    totalW = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'totalW')))
    driver.execute_script("arguments[0].value = '100';", totalW)
    driver.execute_script("arguments[0].dispatchEvent(new Event('input'));", totalW)
    print(Fore.GREEN + "✅ กรอกคะแนนสอบสัมภาษณ์สำเร็จ")
except Exception as e:
    print(Fore.RED + f"❌ ไม่พบช่องกรอกคะแนนสอบสัมภาษณ์: {e}")

try:
    pointinpassW = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'pointinpassW')))
    driver.execute_script("arguments[0].value = '60';", pointinpassW)
    driver.execute_script("arguments[0].dispatchEvent(new Event('input'));", pointinpassW)
    print(Fore.GREEN + "✅ กรอกเกณฑ์คะแนนสอบสัมภาษณ์สำเร็จ")
except Exception as e:
    print(Fore.RED + f"❌ ไม่พบช่องเกณฑ์คะแนนสอบสัมภาษณ์: {e}")

try:
    totalI = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'totalI')))
    driver.execute_script("arguments[0].value = '100';", totalI)
    driver.execute_script("arguments[0].dispatchEvent(new Event('input'));", totalI)
    print(Fore.GREEN + "✅ กรอกคะแนนสอบเขียนสำเร็จ")
except Exception as e:
    print(Fore.RED + f"❌ ไม่พบช่องกรอกคะแนนสอบเขียน: {e}")

try:
    pointinpassI = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'pointinpassI')))
    driver.execute_script("arguments[0].value = '60';", pointinpassI)
    driver.execute_script("arguments[0].dispatchEvent(new Event('input'));", pointinpassI)
    print(Fore.GREEN + "✅ กรอกเกณฑ์คะแนนสอบเขียนสำเร็จ")
except Exception as e:
    print(Fore.RED + f"❌ ไม่พบช่องเกณฑ์คะแนนสอบเขียน: {e}")

    remarkCriterionPoint = driver.find_element(By.ID, 'remarkCriterionPoint')
    remarkCriterionPoint.send_keys("ทดสอบการกรอกเกณฑ์คะแนนสำเร็จ")
    print(Fore.GREEN + "✅ กรอกข้อความเพิ่มเติมสำเร็จ")

    add = driver.find_element(By.ID, 'grid-action-add')
    add.click()
    print(Fore.GREEN + "✅ คลิกปุ่ม Add สำเร็จ")
    
finally:
    input(Fore.CYAN + "📌 กดปุ่ม Enter เพื่อจบการทำงาน...")
    driver.quit()

import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://172.26.3.11:8080/jw/web/login")
driver.implicitly_wait(10)

username = driver.find_element(By.ID, 'j_username')
password = driver.find_element(By.ID, 'j_password')
login = driver.find_element(By.NAME, 'submit')

username.send_keys('dusit.bua')
password.send_keys('dusit.bua')
login.click()

a = input("ป้อนค่าที่ต้องการ: ")  # ใช้ `input` ให้ถูกต้อง
print("ป้อนค่าที่ต้องการ:", a)   # ใช้ `,` ได้ใน `print` แต่ไม่ใช้กับ `input`

driver.get('http://172.26.3.11:8080/jw/web/userview/HRM_Recruitment/v/_/Welcome')
print("ไปยังหน้า Welcome สำเร็จ")

driver.implicitly_wait(10)
input('Press Enter to continue...')
driver.quit()
 
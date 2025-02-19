import time
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



driver = webdriver.Chrome()
try:
    driver.get('http://172.26.3.11:8080/jw/web/login')

    username = driver.find_element(By.ID, 'j_username')
    password = driver.find_element(By.ID,'j_password')
    login = driver.find_element(By.NAME,'submit')

    username.send_keys('dusit.bua')
    password.send_keys('dusit.bua')
    login.click()

    if username.is_displayed():
        print('พบฟิลด์Username')
    else:
        print('ไม่พบฟิลด์Username')
    if password.is_displayed():
        print('พบฟิลด์รหัสผ่าน')
    else: 
        print('ไม่พบฟิดล์รหัสผ่าน')
    
    driver.implicitly_wait(10)

    driver.get('http://172.26.3.11:8080/jw/web/userview/gd_SelfService/gdSelfService/_/welcome')
finally:

    input('กดปุ่มEnter เพื่อจบการทํางาน')
    driver.quit()
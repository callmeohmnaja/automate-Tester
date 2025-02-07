from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()  

try:
    # เปิดหน้าเว็บ Login
    driver.get("http://172.26.3.11:8080/jw/web/login")
    
    # กรอกข้อมูล Login
    username = driver.find_element(By.ID, 'j_username')
    password = driver.find_element(By.ID, 'j_password')
    login = driver.find_element(By.NAME, 'submit')

    username.send_keys("dusit.bua")
    password.send_keys("dusit.bua")
    login.click()


    driver.implicitly_wait(10)  

 
    target_element = driver.find_element(
        By.XPATH, "//span[contains(@class, 'userview-icon') and contains(@style, '/jw/web/app/gd_SelfService/resources/Employee_Self_Service192.png')]"
    )
    target_element.click()

   

    goto = driver.find_element(By.CLASS_NAME, '/jw/web/userview/gd_SelfService/leaveRequest/_/welcome')
    goto.click()

    username.send_keys("dusit.bua")
    password.send_keys("dusit.bua")
    driver.WebDriverWait(driver, 10)


finally:
    input("กดปุ่ม Enter เพื่อจบการทำงาน...")
    driver.quit()


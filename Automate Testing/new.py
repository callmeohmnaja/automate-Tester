from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

try:    
    driver.get("http://172.26.3.11:8080/jw/web/login")

    username = driver.find_element(By.ID, 'j_username')
    password = driver.find_element(By.ID, 'j_password')
    login = driver.find_element(By.NAME, 'submit')

    username.send_keys("dusit.bua")
    password.send_keys("dusit.bua")
    login.click()

finally:
    input("กดปุ่ม Enter เพื่อจบการทำงาน...")
    driver.quit()
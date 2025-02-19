import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from colorama import Fore, Style, init

init(autoreset=True)

driver = webdriver.Chrome()

driver.get("http://172.26.3.11:8080/jw/web/login")

username = driver.find_element(By.ID, 'j_username')
password = driver.find_element(By.ID, 'j_password')
login = driver.find_element(By.NAME, 'submit')

if username.is_displayed():
    print(Fore.GREEN + "พบฟิลด์ username")
else:
    print(Fore.RED + 'ไม่พบฟิลด์ username')
if password.is_displayed():
    print(Fore.GREEN + "พบฟิลด์ password")
else:
    print(Fore.RED + 'ไม่พบฟิลด์ password')
    
username.send_keys('dusit.bua')
password.send_keys('dusit.bua')
login.click()

if driver.current_url == 'http://172.26.3.11:8080/jw/web/userview/appcenter/JogetGistda/_/home':
    print(Fore.GREEN + 'เข้าสู่ระบบสำเร็จ')
else:
    print(Fore.RED + 'เข้าสู่ระบบไม่สำเร็จ')

input(Fore.BLUE + "ป้อนค่าที่ต้องการเพื่อจบการทําง๊าน: ")  
driver.quit()



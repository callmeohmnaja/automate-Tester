import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import colorama
from colorama import Fore, Style, init

init(autoreset=True)

driver = webdriver.Chrome()

driver.get('http://127.0.0.1:5500/index.html')

name = driver.find_element(By.ID, 'name')
name.send_keys('OHM')

if name.is_displayed():
    print(Fore.GREEN + "✅ พบฟิลด์ name😎")
else:
    print(Fore.RED + '❌ ไม่พบฟิลด์ name😡')



driver.implicitly_wait(10)
input('Press Enter to close the automated browser')
driver.quit()



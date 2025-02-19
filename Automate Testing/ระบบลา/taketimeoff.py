import time
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from colorama import init, Fore

driver = webdriver.Chrome()
init(autoreset=True)

try:
        driver.get('http://172.26.3.11:8080/jw/web/login')

        username = driver.find_element(By.ID, 'j_username')
        password = driver.find_element(By.ID,'j_password')
        login = driver.find_element(By.NAME,'submit')

        if username.is_displayed():
            print(Fore.GREEN + 'พบฟิลด์Username')
        else:
            print(Fore.RED + 'ไม่พบฟิลด์Username')
        if password.is_displayed():
            print(Fore.GREEN + 'พบฟิลด์รหัสผ่าน')
        else: 
            print(Fore.RED + 'ไม่พบฟิดล์รหัสผ่าน')

        username.send_keys('dusit.bua')
        password.send_keys('dusit.bua')
        login.click()

        driver.implicitly_wait(10)

        driver.get('http://172.26.3.11:8080/jw/web/userview/gd_SelfService/gdSelfService/_/welcome')
        # driver.get('http://172.26.3.11:8080/jw/web/userview/gd_SelfService/leaveRequest/_/welcome')
        driver.get('http://172.26.3.11:8080/jw/web/userview/gd_SelfService/leaveRequest/_/frmLeave_submit?_action=assignmentView&activityId=7233855_50533_gd_SelfService_process8_newLAform')
        print(Fore.GREEN + 'เข้าสู่แบบฟอร์มลาสําเร็จ')

        #Testcase No.01 ระบบลา
        print(Fore.BLUE + 'ท่านสามาระเปลี่ยนประเภทการป่วยได้ ที่บรรทัด 47 ตรง LeaveType.select_by_value(''ตรงนี้'')')
        # input(Fore.YELLOW + 'Enter เพื่อไปต่อ')
        print(Fore.BLUE + '01=ลาป่วย 05=ลาอุปสมบท พิธีฮัจย์ 08=ลาไปช่วยภริยาคลอดบุตร 03=ลากิจ 07=ลาพักผ่อน')
        LeaveType = Select(driver.find_element(By.NAME, 'LeaveType'))
        LeaveType.select_by_value('01')
        print(Fore.GREEN + 'เลือกประเภทการลาสําเร็จ')

        input(Fore.YELLOW + 'กดEnterเพื่อเริ่มการทํางานTestcase ในลําดับต่อไป')


        whyleave = driver.find_element(By.NAME,'dueTo')
        whyleave.click()
        whyleave.send_keys('สวัสดีครับทดสอบ')

        DateFrom = driver.find_element(By.NAME,'DateFrom')
        DateFrom.click()
        
        input(Fore.BLUE + 'Enterเมื่อกรอกวันที่เสร็จสิ้น')

        DateTo = driver.find_element(By.NAME,'DateTo')
        DateTo.click()

        input(Fore.BLUE +'Enterเพื่อไปต่อ')

        # switch = driver.find_element(By.NAME,'halfAfternoon') ##ไม่ยอมให้กดครึ่งวัน
        # switch.click()

        contact = driver.find_element(By.NAME,'contact')
        contact.click()
        contact.send_keys('ทดสอบการเหตุผล')
        

        # file_input = driver.find_element(By.ID, 'fileUpload') 
        # file_input.send_keys(r"C:\Users\Acer\Desktop\ฝึกงาน\Fake Data\เอกสารอื่นๆ.pdf")  # เปลี่ยนเป็นไฟล์ของคุณ


        uploadfiles = driver.find_element(By.ID, 'fileUpload')  
        uploadfiles.send_keys(r"C:\Users\Acer\Desktop\ฝึกงาน\Fake Data\เอกสารอื่นๆ.pdf")  # เปลี่ยนเป็นไฟล์ของคุณ
        print(Fore.GREEN + 'อัปโหลดไฟล์สำเร็จ')


        assignmentComplete = driver.find_element(By.NAME,'assignmentComplete')
        assignmentComplete.click()

        sum = input(Fore.YELLOW + 'ป้อนค่าเพื่อส่งแบบฟอร์ม')

        if assignmentComplete.input(sum):
            assignmentComplete.click();
        else:
             assignmentComplete.input()
             assignmentComplete.click();
finally:

        input(Fore.GREEN +'กดปุ่มEnter เพื่อจบการทํางาน')
        driver.quit()
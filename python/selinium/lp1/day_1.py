from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import random
from pathlib import Path

#print(Path("../drivers/chromedriver-linux64/chromedriver").is_file())

serv_obj = Service("./drivers/chromedriver-win32/chromedriver")

driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get('http://127.0.0.1:8000')

BASE_DIR = Path(__file__).resolve()

driver.find_element(By.ID,"email").clear()
driver.find_element(By.ID,"email").send_keys("admin@ilensys.com")
driver.find_element(By.ID,"password").clear()
driver.find_element(By.ID,"password").send_keys("At@M@!lEn$y$")

driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

actual_title = driver.title 
expected_title="Laravel | Dashboard"

if actual_title == expected_title:
    print("login test passed")
else:
    print("login failed")

random_int = str(random.randint(1,1000))

driver.find_element(By.PARTIAL_LINK_TEXT,"Manage Subscribers").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Add New Subscriber").click()

driver.find_element(By.XPATH,"//select[@name='company_name']").send_keys("others")

driver.find_element(By.ID,"company_name_other").clear()
driver.find_element(By.ID,"company_name_other").send_keys("Sony")

driver.find_element(By.ID,"division_name").clear()
driver.find_element(By.ID,"division_name").send_keys("Sony div1")

driver.find_element(By.ID,"site_name").clear()
driver.find_element(By.ID,"site_name").send_keys(f"Sony site1{random_int}")

driver.find_element(By.ID,"PrimaryContact").clear()
driver.find_element(By.ID,"PrimaryContact").send_keys("7708958214")

driver.find_element(By.ID,"CustomerEmail").clear()
driver.find_element(By.ID,"CustomerEmail").send_keys(f"sony{random_int}@gmail.com")

driver.find_element(By.ID,"display_name").clear()
driver.find_element(By.ID,"display_name").send_keys(f"Sony Pvt Ltd{random_int}")

driver.find_element(By.XPATH,"//select[@name='country_code']").send_keys("India +91")

driver.find_element(By.ID,"CustomerPhone").clear()
driver.find_element(By.ID,"CustomerPhone").send_keys("1234567890")

driver.find_element(By.XPATH,"/html/body/div[1]/div/div/section/div/div[2]/div/form/input[3]").click()

driver.find_element(By.PARTIAL_LINK_TEXT,"User Management").click()
sleep(1)
driver.find_element(By.XPATH,"//a[normalize-space()='Operations Team']").click()

#db_admin ----------------------------------------------------------------------------- -
driver.find_element(By.XPATH,"//a[normalize-space()='Add New Opsteam User']").click()


driver.find_element(By.XPATH,"//input[@id='name']").clear()
driver.find_element(By.XPATH,"//input[@id='name']").send_keys(f"dbadmin{random_int}")

driver.find_element(By.XPATH,"//input[@id='email']").clear()
driver.find_element(By.XPATH,"//input[@id='email']").send_keys(f"dbadmin{random_int}@ilensys.com")

driver.find_element(By.XPATH,"//select[@id='auth-type']").send_keys("Atom")

driver.find_element(By.XPATH,"//input[@id='password']").clear()
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Ilensys@123")

driver.find_element(By.XPATH,"//input[@id='addrow']").click()

driver.find_element(By.CSS_SELECTOR,"select[name='roles[]']").send_keys("dbAdmin")
#driver.find_element(By.CSS_SELECTOR,"select[name='subscribers[]']").send_keys(f"Sony Pvt Ltd{random_int}")

driver.find_element(By.XPATH,"//input[@value='Create']").click()

#approver -------------------------------------------------------------------------------------
driver.find_element(By.XPATH,"//a[normalize-space()='Add New Opsteam User']").click()


driver.find_element(By.XPATH,"//input[@id='name']").clear()
driver.find_element(By.XPATH,"//input[@id='name']").send_keys(f"approver{random_int}")

driver.find_element(By.XPATH,"//input[@id='email']").clear()
driver.find_element(By.XPATH,"//input[@id='email']").send_keys(f"approver{random_int}@ilensys.com")

driver.find_element(By.XPATH,"//select[@id='auth-type']").send_keys("Atom")

driver.find_element(By.XPATH,"//input[@id='password']").clear()
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Ilensys@123")

driver.find_element(By.XPATH,"//input[@id='addrow']").click()

driver.find_element(By.CSS_SELECTOR,"select[name='roles[]']").send_keys("approver")
driver.find_element(By.CSS_SELECTOR,"select[name='subscribers[]']").send_keys(f"Sony Pvt Ltd{random_int}")

driver.find_element(By.XPATH,"//input[@value='Create']").click()

#author ------------------------------------------------------------------------------------------
driver.find_element(By.XPATH,"//a[normalize-space()='Add New Opsteam User']").click()


driver.find_element(By.XPATH,"//input[@id='name']").clear()
driver.find_element(By.XPATH,"//input[@id='name']").send_keys(f"author{random_int}")

driver.find_element(By.XPATH,"//input[@id='email']").clear()
driver.find_element(By.XPATH,"//input[@id='email']").send_keys(f"author{random_int}@ilensys.com")

driver.find_element(By.XPATH,"//select[@id='auth-type']").send_keys("Atom")

driver.find_element(By.XPATH,"//input[@id='password']").clear()
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Ilensys@123")

driver.find_element(By.XPATH,"//input[@id='addrow']").click()

driver.find_element(By.CSS_SELECTOR,"select[name='roles[]']").send_keys("author")
driver.find_element(By.CSS_SELECTOR,"select[name='subscribers[]']").send_keys(f"Sony Pvt Ltd{random_int}")

driver.find_element(By.XPATH,"//input[@value='Create']").click()

#coordianator ------------------------------------------------------------------------------------------
driver.find_element(By.XPATH,"//a[normalize-space()='Add New Opsteam User']").click()


driver.find_element(By.XPATH,"//input[@id='name']").clear()
driver.find_element(By.XPATH,"//input[@id='name']").send_keys(f"coordinator{random_int}")

driver.find_element(By.XPATH,"//input[@id='email']").clear()
driver.find_element(By.XPATH,"//input[@id='email']").send_keys(f"coord{random_int}@ilensys.com")

driver.find_element(By.XPATH,"//select[@id='auth-type']").send_keys("Atom")

driver.find_element(By.XPATH,"//input[@id='password']").clear()
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Ilensys@123")

driver.find_element(By.XPATH,"//input[@id='addrow']").click()

driver.find_element(By.CSS_SELECTOR,"select[name='roles[]']").send_keys("coordinator")
driver.find_element(By.CSS_SELECTOR,"select[name='subscribers[]']").send_keys(f"Sony Pvt Ltd{random_int}")

driver.find_element(By.XPATH,"//input[@value='Create']").click()
driver.find_element(By.XPATH,"//a[@class='nav-link logout']").click()

#_____________________________________________________________________________________________________________
#______________________________________________________ DB ADMIN ROLE   ________________________________________
#______________________________________________________________________________________________________________


driver.find_element(By.ID,"email").clear()
driver.find_element(By.ID,"email").send_keys(f"dbadmin{random_int}@ilensys.com")
driver.find_element(By.ID,"password").clear()
driver.find_element(By.ID,"password").send_keys("Ilensys@123")

driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()


#Manufacturer_excel file
driver.find_element(By.XPATH,"//a[normalize-space()='Workspace']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Upload']").click()

driver.find_element(By.XPATH,"//label[normalize-space()='Upload Manufacturers']").click()

driver.find_element(By.NAME,"import_file").send_keys("D:\python\selinium\DS-1\manufacturer.xlsx")

driver.find_element(By.XPATH,"//input[@name='overwrite']").click()
sleep(1)
#driver.find_element(By.NAME,"clear_exist").click()

driver.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()

#Master_excel file
driver.find_element(By.XPATH,"//a[normalize-space()='Workspace']").click()
sleep(1)
driver.find_element(By.XPATH,"//a[normalize-space()='Upload']").click()

driver.find_element(By.XPATH,"//label[normalize-space()='Upload Master Components']").click()

driver.find_element(By.NAME,"import_file").send_keys("D:\python\selinium\DS-1\master.xlsx")

driver.find_element(By.XPATH,"//input[@name='overwrite']").click()
sleep(1)
driver.find_element(By.NAME,"clear_exist").click()

driver.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()

driver.find_element(By.XPATH,"//a[@class='nav-link logout']").click()

#_____________________________________________________________________________________________________________
#______________________________________________________ Approver ADMIN ROLE   ________________________________________
#______________________________________________________________________________________________________________

driver.find_element(By.ID,"email").clear()
driver.find_element(By.ID,"email").send_keys(f"approver{random_int}@ilensys.com")
driver.find_element(By.ID,"password").clear()
driver.find_element(By.ID,"password").send_keys("Ilensys@123")

driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

driver.find_element(By.XPATH,"//a[normalize-space()='Workspace']").click()
sleep(1)
driver.find_element(By.XPATH,"//a[normalize-space()='Upload']").click()

driver.find_element(By.XPATH,"//label[normalize-space()='Upload - New BOM']").click()

driver.find_element(By.XPATH,"//a[@id='addProduct']").click()
sleep(1)

driver.find_element(By.NAME,"product_name").clear()
driver.find_element(By.ID,"product_name").send_keys(f"Laptop{random_int}")
driver.find_element(By.XPATH,"//input[@value='Submit']").click()

driver.find_element(By.XPATH,"//select[@name='product_id']").send_keys(f"Laptop{random_int}")

driver.find_element(By.NAME,"bom_name").clear()
driver.find_element(By.NAME,"bom_name").send_keys(f"Bom1{random_int}")

driver.find_element(By.NAME,"revision").clear()
driver.find_element(By.NAME,"revision").send_keys(f"{random_int}")

driver.find_element(By.XPATH,"//textarea[@id='description']").clear()
driver.find_element(By.XPATH,"//textarea[@id='description']").send_keys(f"bom desciption{random_int}")

driver.find_element(By.NAME,"import_file").send_keys("D:\python\selinium\DS-1\/bom.xlsx")

driver.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()

driver.find_element(By.XPATH,"//a[normalize-space()='Broadcast']").click()

driver.find_element(By.XPATH,"//a[@class='nav-link logout']").click()
sleep(10)
    
driver.close()


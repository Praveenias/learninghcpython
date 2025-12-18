from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import random
import requests as requests
from pathlib import Path


serv_obj = Service("D:\browser_Drivers\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get('http://127.0.0.1:8000')

BASE_DIR = Path(__file__).resolve()

driver.find_element(By.ID,"email").clear()
driver.find_element(By.ID,"email").send_keys("coord@ilensys.com")
driver.find_element(By.ID,"password").clear()
driver.find_element(By.ID,"password").send_keys("Ilensys@123")

driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

unwanted_links = ('java','php','http://127.0.0.1:8000/logout')

#links = [ele.get_attribute("href") for ele in driver.find_elements(By.XPATH,"//a[@href]")]

link_dict={}
def generate_link(url_link,links=[]):
  if url_link in link_dict:
    return False
  if url_link.startswith(unwanted_links):
    return False
  
  res = requests.head(url_link)
  if res.status_code >= 400:
    link_dict[url_link] = False
    return False
  else:
    link_dict[url_link] = True
  driver.find_element(By.CSS_SELECTOR,f"a[href={url_link}]").click()
  links_ = [ele.get_attribute("href") for ele in driver.find_elements(By.XPATH,"//a[@href]")]
  for link in links:
    generate_link(link,links_)
   
#generate_link('http://127.0.0.1:8000/dashboard',[])
driver.find_element(By.CSS_SELECTOR,"a[href='http://127.0.0.1:8000/dashboard']").click()
print(link_dict)
    
    

#print(links)
# for url_link in links:
#   if url_link.startswith(unwanted_links):
#     continue
#   res = requests.head(url_link)
#   #print(f'{url_link} came with status code {res.status_code}')
#   if res.status_code >= 400:
#      print(url_link," is broken link ")


driver.close()
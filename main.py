from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import sys
import time

# get login credentials and validation of argumnets
if len(sys.argv) == 4:
    email = sys.argv[1]
    password = sys.argv[2]
    post_url = sys.argv[3]
    
else:
    print("Error - Introduce los argumentos correctamente")
    print('Ejemplo: main.py "email" "password" "post_url"')  
    exit()

# create a new Chrome session

driver = webdriver.Chrome('./chromedriver.exe')
driver.maximize_window()

# log in
driver.get("https://www.facebook.com")
search_field = driver.find_element_by_id("email")
search_field.send_keys(email)
search_field = driver.find_element_by_id("pass")
search_field.send_keys(password)
search_field.submit()
time.sleep(5)

#access to post on facebook
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'t')# +CTRL+T nueva pestana
driver.get(post_url)
print("Logged in as " + email)

# downloads html page from url to manipulate with BeautifulSoup
page_source1 = driver.page_source
pageWebContent = soup(page_source1, "lxml")

containers = pageWebContent.findAll("li")
listUsers = []
for ElementOnContainers in containers:
    comments = ElementOnContainers.find("span",{"class":"pq6dq46d"})

    if comments is None :
        print("")
    else:
        users = comments.find_all('span',class_='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb mdeji52x e9vueds3 j5wam9gi lrazzd5p oo9gr5id')
        if len(users)==1:
            listUsers.append(users[0].get_text())
        
            
    
print(listUsers)

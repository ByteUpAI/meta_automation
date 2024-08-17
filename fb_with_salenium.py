from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

PATH = 'C:/Users/raush/chromedriver-win64/chromedriver-win64/chromedriver.exe'

service = Service(PATH)

driver = webdriver.Chrome(service=service)

# Target URL
target_url = "https://www.facebook.com/involvehealth"

driver.get(target_url)
time.sleep(5)

resp = driver.page_source
driver.close()

soup = BeautifulSoup(resp, 'html.parser')

l = []

items = soup.find_all('div', {'class': 'x9f619 x1n2onr6 x1ja2u2z x78zum5 x2lah0s x1qughib x1qjc9v5 xozqiw3 x1q0g3np x1pi30zi x1swvt13 xyamay9 xykv574 xbmpl8g x4cne27 xifccgj'})[1]

o = {}
allDetails = items.find_all("div", {"class": "x9f619 x1n2onr6 x1ja2u2z x78zum5 x2lah0s x1nhvcw1 x1qjc9v5 xozqiw3 x1q0g3np xyamay9 xykv574 xbmpl8g x4cne27 xifccgj"})

for contact in allDetails:
    checkaddress = len(contact.text.split(","))
    if checkaddress > 2:
        o["address"] = contact.text
        continue
    
    checknumber = len(contact.text.split("-"))
    if checknumber > 2:
        o["number"] = contact.text
        continue
    
    if '@' in contact.text:
        o["email"] = contact.text
        continue

span_content = soup.find('span', {'class': 'html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs'})
if span_content:
    o["span_text"] = span_content.text

l.append(o)
print(l)

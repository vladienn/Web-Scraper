import requests
import urllib
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


option = Options()
option.add_argument("--disable-notifications")
option.add_argument("disable-infobars")
driver = webdriver.Chrome(chrome_options = option)

f = open("dataFacebook.txt", "w")

def login():
	driver.get("https://www.facebook.com/")
	elementID = driver.find_element_by_id("email")
	elementID.send_keys("prezentaciqpogeo@abv.bg")

	elementID = driver.find_element_by_id("pass")
	elementID.send_keys("pythonScraper")

	elementID.submit()

def scrapeProfile(url):
	try:
		driver.get(url)
		driver.get(url)
		bs = BeautifulSoup(driver.page_source, "html.parser")
	
		info = bs.findAll("div", {"class":"_50f3"})
		for i in info:
			print(i.get_text(' ', strip=True))
		img_url = bs.find("img",{"class":"_11kf img"})["src"]
		
		print("")
		driver.get(url +"/likes_all")
		bs_likes = BeautifulSoup(driver.page_source, "html.parser")
		likes_all = bs_likes.findAll("div", {"class":"fsl fwb fcb"})

		cnt = 0
		for l in likes_all:
			if(cnt<10):
				print(l.get_text(" ", strip=True))
				cnt+=1
			else:
				break
	except AttributeError:
		print("Attribute Error")
	
login()
scrapeProfile("https://www.facebook.com/ysmin.biserova")
f.close()

#_c24 _50f4

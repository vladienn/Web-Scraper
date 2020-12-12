import requests
import urllib
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome()
f = open("dataLinkedIn.txt", "w")

def login():
	driver.get("https://www.linkedin.com/login")
	elementID = driver.find_element_by_id("username")
	elementID.send_keys("vladien@abv.bg")

	elementID = driver.find_element_by_id("password")
	elementID.send_keys("pythonScraper")

	elementID.submit()

def scrapeProfile(url):
	driver.get(url)
	bs = BeautifulSoup(driver.page_source, "html.parser")
	
	profile_img_url = bs.find("img", {"id":"ember55"})["src"]
	f.write(profile_img_url + "\n")
	
	name = bs.find("li", {"class":"inline t-24 t-black t-normal break-words"}).get_text(', ', strip=True)
	f.write(name + "\n")
	
	urllib.request.urlretrieve(profile_img_url, (name + ".jpg"))

	occupation = bs.find("h2", {"class":"mt1 t-18 t-black t-normal break-words"}).get_text(', ', strip=True)
	f.write(occupation + "\n")

	location = bs.find("li", {"class":"t-16 t-black t-normal inline-block"}).get_text(', ', strip=True)
	f.write(location + "\n\n")
	
	experience = bs.find("section", {"id":"experience-section"}).findAll("a")
	f.write("Experience\n")
	for xp in experience:
		img_url = xp.img["src"]
		f.write(img_url + "\n")
		
		workplace_role = xp.h3.get_text(', ', strip=True)
		f.write(workplace_role + "\n")
		
		workplace_name = xp.find("p", {"class":"pv-entity__secondary-title t-14 t-black t-normal"}).get_text(', ', strip=True)
		f.write(workplace_name + "\n\n")
		
		dates_employed = xp.find("h4", {"class":"pv-entity__date-range t-14 t-black--light t-normal"})
		dates_employed = dates_employed.findAll("span")[1].get_text(', ', strip=True)
		f.write(dates_employed + "\n")
	education = bs.find("section", {"id":"education-section"}).findAll("a")
	f.write("Education\n")
	for ed in education:
		school_name = ed.h3.get_text(', ', strip=True)
		f.write(school_name + "\n")
		
		degree = ed.findAll("span", {"class":"pv-entity__comma-item"})
		for dg in degree:
			f.write(dg.get_text(', ', strip=True) + "   ")
		f.write("\n")
		
		dates_attended = ed.findAll("time")
		f.write(dates_attended[0].get_text(', ', strip=True)+ " - " +dates_attended[1].get_text(', ', strip=True)+"\n\n")
	
	
	
login()
scrapeProfile("https://www.linkedin.com/in/filip-andonov-478204a6/")
#scrapeProfile("https://www.linkedin.com/in/boris-staykov-8410796/")
f.close()


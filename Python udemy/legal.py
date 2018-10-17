import requests
from bs4 import BeautifulSoup
from csv import writer
import re

res=requests.get("http://www.legalserviceindia.com/lawyers/delhi.htm")
# print(res.text)
soup=BeautifulSoup(res.text, "html.parser")
articles=soup.find_all(class_="law-block")
articles1=soup.find_all("tr")
# print(articles1)
# print(articles1.get_text())
# print(articles)


with open("legaldata.csv","w") as csv_file:
	csv_writer=writer(csv_file)	
	csv_writer.writerow(["Name","Email","contact","Address"])

	for arti in articles:
		a_tag=arti.find("h2")
		# print(a_tag)
		name=a_tag.get_text()
		# print(name)
		e_tag=arti.find("font")
		email=e_tag.get_text()
		# print(email)
		address=arti.find(text=lambda text:text and "Add" in text)
		# print(address)
		telephone=arti.find(text=re.compile("^User "))
		# print(telephone)
		csv_writer.writerow([name,email,telephone,address])
import requests
from bs4 import BeautifulSoup
from csv import writer


res=requests.get("https://www.rithmschool.com/blog")
# print(res.text)
soup=BeautifulSoup(res.text, "html.parser")
articles=soup.find_all("article")
# print(articles)



with open("blog_data.csv","w") as csv_file:
	csv_writer=writer(csv_file)
	csv_writer.writerow(["Title","Link","Date"])


	for arti in articles:
		a_tag=arti.find("a")
		title=a_tag.get_text()
		# print(a_tag["href"])
		url=a_tag["href"]
		# date
		# print(arti.find("time")["datetime"])
		date=arti.find("time")["datetime"]
		# print(title,url,date)
		csv_writer.writerow([title,url,date])
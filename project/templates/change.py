import glob
import os 
import urllib
from bs4 import BeautifulSoup
l = glob.glob("/home/bhavana/Documents/sem 7/SE/templates/*.html")
for file_name in l :
	print("hi",file_name)
	page = urllib.urlopen(file_name)
	soup = BeautifulSoup(page,"html")
	soup.prettify()
	href_tags = soup.find_all('link',href=True)	
	src_tags = soup.find_all(src=True)
	for tag in href_tags :
		print(tag['href'])
		if tag['href'].split("/")[0] == "static" :
			print("hello")
			tag['href'] = "{{ url_for('static', filename='" + tag['href'][7:]  + "') }}"
			print tag['href']
		
	for tag in src_tags :
		print(tag['src'])
		if tag['src'].split("/")[0] == "static" :
			print("hello")
			tag['src'] = "{{ url_for('static', filename='" + tag['src'][7:]  + "') }}"
			print tag['src']
	with open(file_name,"w") as f :
		f.write(str(soup))

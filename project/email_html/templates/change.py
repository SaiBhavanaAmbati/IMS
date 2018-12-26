import glob
import os 
import pandas as pd
import urllib
l = glob.glob("/home/bhavana/Documents/sem 7/SE/project/templates/*.html")
for file_name in l :
	f = urllib.urlopen(file_name)
	lines = f.read()
	i = 0  
	for line in lines :
		if i < 10 :
			print(line)
		else : break
		i =  i +1 
		

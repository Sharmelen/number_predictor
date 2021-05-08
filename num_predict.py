import datetime
# import tensorflow
import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.pylab import rcParams
# rcParams['figure.figsize']=20,10
# from keras.models import Sequential
# from keras.layers import LSTM,Dropout,Dense
# from sklearn.preprocessing import MinMaxScaler
import xlsxwriter

from bs4 import BeautifulSoup
import requests

base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(3780)]

f = open("4D_NUMBERS.txt","w")

all_prize = []

for z in range (3780):

	try:
		
	
		date_only = str(date_list[z]).split(" ")
		#print(date_only[0])

		page = requests.get("https://www.check4d.com/past-results/"+str(date_only[0]))
		#page = requests.get("https://www.check4d.com/past-results/2021-05-05")

		soup = BeautifulSoup(page.content, 'html.parser')
		top_result = soup.find_all('td', class_='resulttop')

		main_prize = []
		
		main_prize.append(date_only[0])
		
		for x in range (3):
			result_one = str(top_result[x]).replace('<td class="resulttop" style="width:55%">',"")
			result_two = result_one.replace('<td class="resulttop">',"")
			first_prize = result_two.replace("</td>","")

			main_prize.append(first_prize)

		bottom_result = soup.find_all('td', class_='resultbottom')

		rest_prize = []

		for y in range(23):
			result_one = str(bottom_result[y]).replace('<td class="resultbottom">','')
			result_two = result_one.replace("</td>","")
			rest_prize.append(result_two)
			
		joined_prize = main_prize+rest_prize
		f.write(joined_prize[0]+","+joined_prize[1]+","+joined_prize[2]+","+joined_prize[3]+","+joined_prize[4]+","+joined_prize[5]+","+joined_prize[6]+","+joined_prize[7]+","+joined_prize[8]+","+joined_prize[9]+","+joined_prize[10]+","+joined_prize[11]+","+joined_prize[12]+","+joined_prize[13]+","+joined_prize[14]+","+joined_prize[15]+","+joined_prize[16]+","+joined_prize[17]+","+joined_prize[18]+","+joined_prize[19]+","+joined_prize[20]+","+joined_prize[21]+","+joined_prize[22]+","+joined_prize[23]+","+joined_prize[24]+","+joined_prize[25]+","+joined_prize[26]+"\n")
		print("DATA RECORDED")
	
	
		
	#print(all_prize)
	
	except:
		print("DATA NOT AVAILABLE")
		
f.close()

		
	



	

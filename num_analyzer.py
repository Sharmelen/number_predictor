import pandas
from collections import Counter
import os,sys
import itertools






def high_prob_occur(comb_num):
	combined_number = comb_num[0]+comb_num[1]+comb_num[2]+comb_num[3]

	excel_data_df = pandas.read_excel('4D_NUM_LATEST.xlsx', sheet_name='Sheet1')
	all_collumns = excel_data_df.columns.ravel()

	all_collumns = list(all_collumns)
	#print(all_collumns)
	collector = []
	magic_num = []
	for x in range(len(all_collumns)-1):
		col_number = all_collumns[x+1]
		all_num_list = excel_data_df[col_number].tolist()
		collector.append(all_num_list)
		
	for y in range (len(collector)):
		for z in range (len(collector[y])):
			over_num = collector[y]
			spec_num = over_num[z]
			
			if spec_num == int(combined_number):
			
				magic_num.append(combined_number)
				
	print(str(combined_number)+" has occured "+str(len(magic_num)))

	
		
def statistics():

	path = "occur_num/"
	dirs = os.listdir( path )
	sumation = 0
	
	num_dict = {}
	all_num = []
	
	for x in range (len(dirs)):
		single_file = dirs[x]
		change_1 = str(single_file).replace("num_","")
		new_name = change_1.replace(".txt","")
		
		if new_name == "zero":
			new_name = "0"
			
		if new_name == "one":
			new_name = "1"
			
		if new_name == "two":
			new_name = "2"
			
		if new_name == "three":
			new_name = "3"
			
		if new_name == "four":
			new_name = "4"
			
		if new_name == "five":
			new_name = "5"
			
		if new_name == "six":
			new_name = "6"
			
		if new_name == "seven":
			new_name = "7"
			
		if new_name == "eight":
			new_name = "8"
			
		if new_name == "nine":
			new_name = "9"
			
		
		full_dir = "occur_num/"+single_file
		f = open(full_dir,"r")
		read_text = f.read()
		split_text = read_text.split(",")
		
		
		for y in range (len(split_text)-1):
			
			sumation += int(split_text[y])
			
			
		#print(new_name+" has occured ",sumation," times\n")
		num_dict[new_name] = sumation
		all_num.append(sumation)
	
	
	sorted_num = sorted(all_num,reverse=True)
	
	key_one = [k for k, v in num_dict.items() if v == sorted_num[0]]
	key_two = [k for k, v in num_dict.items() if v == sorted_num[1]]
	key_three = [k for k, v in num_dict.items() if v == sorted_num[2]]
	key_four = [k for k, v in num_dict.items() if v == sorted_num[3]]
	
	
	high_prob_num = [key_one[0],key_two[0],key_three[0],key_four[0]]
	permutation = list(itertools.permutations(high_prob_num,4))
	for x in range(len(permutation)):
		comb_num = permutation[x]
		high_prob_occur(comb_num)
	
	
	
	
statistics()

# def single_num(all_key):
	# f_zero = open("occur_num/num_zero.txt","a")
	# f_one = open("occur_num/num_one.txt","a")
	# f_two = open("occur_num/num_two.txt","a")
	# f_three = open("occur_num/num_three.txt","a")
	# f_four = open("occur_num/num_four.txt","a")
	# f_five = open("occur_num/num_five.txt","a")
	# f_six = open("occur_num/num_six.txt","a")
	# f_seven = open("occur_num/num_seven.txt","a")
	# f_eight = open("occur_num/num_eight.txt","a")
	# f_nine = open("occur_num/num_nine.txt","a")
	
	
	# num_zero = 0
	# num_one = 0
	# num_two = 0
	# num_three = 0
	# num_four = 0
	# num_five = 0
	# num_six = 0
	# num_seven = 0
	# num_eight = 0
	# num_nine = 0
	
	# for x in range (len(all_key)):
		# single_num = all_key[x]
		
		# if "0" in single_num:	
			# num_zero +=1
			
		# if "1" in single_num:
			# num_one += 1
		
		# if "2" in single_num:
			# num_two +=1
			
		# if "3" in single_num:
			# num_three +=1
			
		# if "4" in single_num:
			# num_four +=1
			
		# if "5" in single_num:
			# num_five +=1
			
		# if "6" in single_num:
			# num_six +=1
			
		# if "7" in single_num:
			# num_seven +=1
			
		# if "8" in single_num:
			# num_eight +=1
			
		# if "9" in single_num:
			# num_nine +=1
			
	# f_zero.write(str(num_zero)+",")
	# f_one.write(str(num_one)+",")
	# f_two.write(str(num_two)+",")
	# f_three.write(str(num_three)+",")
	# f_four.write(str(num_four)+",")
	# f_five.write(str(num_five)+",")
	# f_six.write(str(num_six)+",")
	# f_seven.write(str(num_seven)+",")
	# f_eight.write(str(num_eight)+",")
	# f_nine.write(str(num_nine)+",")
	
	# f_zero.close()
	# f_one.close()
	# f_two.close()
	# f_three.close()
	# f_four.close()
	# f_five.close()
	# f_six.close()
	# f_seven.close()
	# f_eight.close()
	# f_nine.close()
	
	
	
# def num_occur(col_number):
	# #if col_number == "first_prize":

	# numbers = excel_data_df[col_number].tolist()

	# repeat_num = dict(Counter(numbers))

	# key_num = repeat_num.keys()
	# key_list = list(key_num)

	# all_key = []

	# for x in range (len(key_list)):
		# counter = repeat_num[key_list[x]]
		# counter = int(counter)
		
		# if counter > 1: #The occurance of same number multiple times
			# try:
				# if len(str(key_list[x]))<2:
					# new_key = str(key_list[x])+"000"
					
				# elif len(str(key_list[x]))<3:
					# new_key = str(key_list[x])+"00"
					
				# elif len(str(key_list[x]))<4:
					# new_key = str(key_list[x])+"0"
				# else:
					# new_key = str(key_list[x])
					
				# int(key_list[x])
				
				# #print(str(new_key)+"--->"+str(counter))
				
				# all_key.append(str(new_key))
				
			# except:
				# print("")
			
	# single_num(all_key)
		
	
	

# excel_data_df = pandas.read_excel('4D_NUM_LATEST.xlsx', sheet_name='Sheet1')

# # date = excel_data_df["Date"].tolist()
# # print(date[0])

# all_collumns = excel_data_df.columns.ravel()
# all_collumns = list(all_collumns)

# for x in range(len(all_collumns)-1):
	# col_number = all_collumns[x+1]
	
	# num_occur(col_number)
	


	
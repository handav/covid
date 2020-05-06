import pandas as pd
import json
import matplotlib.pyplot as plt

# this is copied and pasted from the terminal of norm.py, participants by week
#week_meta_info = {'1': 638, '2': 635, '3': 620, '4': 585, '5': 523, '6': 387, '7': 203, '8': 84}
# positive participants
#pos_week_meta_info = {'1': 148, '2': 148, '3': 141, '4': 131, '5': 116, '6': 80, '7': 29, '8': 14}
# # negative participants
# neg_week_meta_info = {'1': 162, '2': 161, '3': 160, '4': 155, '5': 134, '6': 96, '7': 49, '8': 19}

# make sure this is the same as norm.py
num_weeks_to_look_at = 8


for n in range(1, num_weeks_to_look_at+1):
	weeknum = n
	week = "Week_" + str(weeknum)
	csv_file = week + ".csv"
	print(week)
	df = pd.read_csv(csv_file, skipinitialspace=True)
	df = df.sort_values(by=[week], ascending=False)
	#df = df.set_index('Symptom').transpose()
	#print(df['Symptom'].head(10))
	# for i in range(0, 10):
	# 	row = df.iloc[i]
	# 	print(row)
	# 	row = row/week_meta_info[:n]
	# 	print(row)
	out_csv_file = 'top_ten/' +week + "_top10.csv"
	df.head(10).to_csv(out_csv_file, index=False, header=True)
	for r in df['Symptom'].head(10):
		print(df[df['Symptom'] == r].to_string(index=False, header=False))
	print('\n')





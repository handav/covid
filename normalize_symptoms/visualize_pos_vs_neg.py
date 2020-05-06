import pandas as pd
import json
import matplotlib.pyplot as plt

# this is copied and pasted from the terminal of norm.py, participants by week
#week_meta_info = {'1': 638, '2': 635, '3': 620, '4': 585, '5': 523, '6': 387, '7': 203, '8': 84}
# positive participants
# pos_week_meta_info = {'1': 148, '2': 148, '3': 141, '4': 131, '5': 116, '6': 80, '7': 29, '8': 14}
# # negative participants
# neg_week_meta_info = {'1': 162, '2': 161, '3': 160, '4': 155, '5': 134, '6': 96, '7': 49, '8': 19}

pos_week_meta_info = [148, 148, 141, 131, 116, 80, 29, 14]
# negative participants
neg_week_meta_info = [162, 161, 160, 155,  134, 96, 49, 19]


pos_participants = 148
neg_participants = 162

# sets the y axis as percentage of participants
y_axis_percent = 1.0
# make sure this is the same as norm.py
num_weeks_to_look_at = 8


for n in range(3, num_weeks_to_look_at+1):
	weeknum = n
	week = "Week_" + str(weeknum)
	pos_csv_file = week + "positive_results.csv"
	neg_csv_file = week + "negative_results.csv"

	files = [pos_csv_file, neg_csv_file]
	dfs = []

	posdf = pd.read_csv(pos_csv_file, skipinitialspace=True)
	#df_ = df_.sort_values(by=[week], ascending=False)
	posdf = posdf.set_index('Symptom')
	dfs.append(posdf)
	negdf = pd.read_csv(neg_csv_file, skipinitialspace=True)
	#df_ = df_.sort_values(by=[week], ascending=False)
	negdf = negdf.set_index('Symptom')
	dfs.append(negdf)
		#print(df_.head())
	# df = pd.merge(dfs[0], dfs[1], on="Symptom")
	# print('head', df.head())
	# print('LEN', len(dfs[0]))
	# print(dfs[0].head())
	# print(dfs[1].head())

	# # Color for each bar
	# cr = [['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red', 'black']]
	for i in range(0, len(dfs[0])):
		print('I', i)
		row1 = dfs[0].iloc[i]
		print('row 1', row1)
		print(pos_week_meta_info)
		row1 = row1/pos_week_meta_info[:n]
		print('row 1', row1)
		row2 = dfs[1].iloc[i]
		row2 = row2/neg_week_meta_info[:n]
		plt.clf()
		print(pd.diff(row1, row2))
		ax1 = row1.plot(kind='line', y='positive', title=row1.name, ylim=(0, 1.0*y_axis_percent), legend=True)
		ax2 = row2.plot(kind='line', y='negative',legend=True)
		ax1.legend(['Positive', 'Negative'])
		#plt.legend(handles=[row1,row2])
		plt.xlabel('Weeks')
		plt.ylabel('Percentage Affected')
		# Export graph
		if '/' in row1.name:
			imagepath = 'pos_vs_neg_symptoms/' + week + "_" + row1.name.replace("/", "") + ".png"
		else:
			imagepath = 'pos_vs_neg_symptoms/' + week + "_" + row1.name + ".png"
		#print(imagepath)
		#plt.savefig(imagepath)
		#plt.show()
	# 	ax = dfs[0][i].plot(kind='line')
	# 	#ax = dfs[0][i].plot(kind='line', subplots=True, layout=(25, 4), figsize=(20, 40))
	# 	plt.show()
	# for i in range(0,len(ax)):
	# 	for j in range(0, len(ax[0])):
	# 		try:
	# 			ax[i][j].get_legend().remove()
	# 		except:
	# 			continue


	# # Setting the values for all axes.
	# custom_ylim = (0, week_meta_info[str(weeknum)]*highest_count_percentage)
	# plt.setp(ax, ylim=custom_ylim)
	# fig = ax[0][0].get_figure()
	# fig.tight_layout()
	# # Adjust spacing at top
	# fig.subplots_adjust(top=0.99)



	# If you want to see it in real time
	#plt.show()





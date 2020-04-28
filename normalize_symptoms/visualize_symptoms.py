import pandas as pd
import json
import matplotlib.pyplot as plt

# this is copied and pasted from the terminal of norm.py 
week_meta_info = {'1': 464, '2': 462, '3': 455, '4': 422, '5': 370, '6': 271, '7': 118, '8': 41}

for n in range(1, 9):
	weeknum = n
	week = "Week_" + str(weeknum)
	csv_file = week + ".csv"

	df = pd.read_csv(csv_file, skipinitialspace=True)
	df = df.set_index('Symptom').transpose()

	# Color for each bar
	cr = [['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red', 'black']]
	ax = df.plot(kind='bar', subplots=True, layout=(25, 3), figsize=(20, 40), color=cr)
	for i in range(0,len(ax)):
		for j in range(0, len(ax[0])):
			try:
				ax[i][j].get_legend().remove()
			except:
				continue


	# Setting the values for all axes.
	custom_ylim = (0, week_meta_info[str(weeknum)])
	plt.setp(ax, ylim=custom_ylim)
	fig = ax[0][0].get_figure()
	fig.tight_layout()
	# Adjust spacing at top
	fig.subplots_adjust(top=0.99)

	# Export graph
	imagepath = week + ".png"
	plt.savefig(imagepath)

	# If you want to see it in real time
	#plt.show()





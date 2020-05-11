import pandas as pd
import json
import matplotlib.pyplot as plt

# this is copied and pasted from the terminal of norm.py, participants by week
week_meta_info = {'1': 638, '2': 635, '3': 620, '4': 585, '5': 523, '6': 387, '7': 203, '8': 84}
# positive participants
# week_meta_info = {'1': 148, '2': 148, '3': 141, '4': 131, '5': 116, '6': 80, '7': 29, '8': 14}
# negative participants
#week_meta_info = {'1': 162, '2': 161, '3': 160, '4': 155, '5': 134, '6': 96, '7': 49, '8': 19}

# THIS CAN BE 'bar' OR 'line'
graph_type = 'line'

# sets the y axis as percentage of participants
highest_count_percentage = 0.6
# make sure this is the same as norm.py
num_weeks_to_look_at = 8


csv_file = "Symptoms_bypercentage_top10overall.csv"

df = pd.read_csv(csv_file, skipinitialspace=True)
df = df.sort_values(by=['Week_1'], ascending=False)
df = df[:10]
print(df['Symptom'].head(10))
df = df.set_index('Symptom').transpose()
#df.columns=df.columns.str.strip()


if graph_type == 'bar':
	cr = [['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red', 'black']]
	ax = df.plot(kind='bar', subplots=True, layout=(25, 4), figsize=(20, 60), color=cr)
	for i in range(0,len(ax)):
		for j in range(0, len(ax[0])):
			try:
				ax[i][j].get_legend().remove()
				ax[i][j].set_xlabel('Weeks')
				ax[i][j].set_ylabel('Percentage Affected')
			except:
				continue

elif graph_type == 'line':
	ax = df.plot(kind='line', subplots=True, layout=(25, 4), figsize=(20, 60))
	for i in range(0,len(ax)):
		for j in range(0, len(ax[0])):
			try:
				ax[i][j].set_xlabel('Weeks')
				ax[i][j].set_ylabel('Percentage Affected')
			except:
				continue


# Setting the values for all axes. 
#custom_ylim = (0, week_meta_info[str(weeknum)]*highest_count_percentage)
# Setting the values for all axes for percentage
custom_ylim = (0, 60)
plt.setp(ax, ylim=custom_ylim)

fig = ax[0][0].get_figure()
fig.tight_layout()
# Adjust spacing at top
fig.subplots_adjust(top=0.99)

# Export graph
imagepath = "Symptoms_bypercentage_top10overall" + graph_type + ".png"
print(imagepath)
plt.savefig(imagepath)

# If you want to see it in real time
#plt.show()





import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

# this is copied and pasted from the terminal of norm.py, participants by week
week_meta_info = {'1': 638, '2': 635, '3': 620, '4': 585, '5': 523, '6': 387, '7': 203, '8': 84}
# positive participants
# week_meta_info = {'1': 148, '2': 148, '3': 141, '4': 131, '5': 116, '6': 80, '7': 29, '8': 14}
# negative participants
#week_meta_info = {'1': 162, '2': 161, '3': 160, '4': 155, '5': 134, '6': 96, '7': 49, '8': 19}

# THIS CAN BE 'bar' OR 'line'
graph_type = 'line'

# make sure this is the same as norm.py
num_weeks_to_look_at = 8


csv_file = "Symptoms_bypercentage_top10overall.csv"


df = pd.read_csv(csv_file, skipinitialspace=True)
#df = df.sort_values(by=['Week_2'], ascending=False)
df = df[:10]
print(df['Symptom'].head(10))
df = df.set_index('Symptom').transpose()



ax = df.plot(kind='line', title='Top 10 Symptoms', figsize=(11,12), color = ['violet', 'indigo', 'cyan', 'blue', 'green', 'olive', 'yellow', 'gold', 'orange', 'red', 'black', 'brown'])
ax.set_xlabel('Weeks')
ax.set_ylabel('Percentage Affected')
plt.legend(fontsize='small')


# Setting the values for all axes. 
#custom_ylim = (0, week_meta_info[str(weeknum)]*highest_count_percentage)
# Setting the values for all axes for percentage
custom_ylim = (0, 60)
plt.setp(ax, ylim=custom_ylim)

# fig = ax[0][0].get_figure()
# fig.tight_layout()
# # Adjust spacing at top
# fig.subplots_adjust(top=0.99)

# # Export graph
imagepath = "Symptoms_bypercentage_top10_overall" + graph_type + ".png"
print(imagepath)
plt.savefig(imagepath)

# If you want to see it in real time
plt.show()





import pandas as pd
import json
import matplotlib.pyplot as plt

df = pd.read_csv("4_25_symptoms_by_week.csv", skipinitialspace=True)
df = df.set_index('Symptom').transpose()

ax = df.plot(kind='bar', subplots=True, layout=(25, 3), figsize=(20, 40))
for i in range(0,len(ax)):
	for j in range(0, len(ax[0])):
		try:
			ax[i][j].get_legend().remove()
		except:
			continue


# Setting the values for all axes.
custom_ylim = (0, 250)
plt.setp(ax, ylim=custom_ylim)
fig = ax[0][0].get_figure()
fig.tight_layout()
# Adjust spacing at top
fig.subplots_adjust(top=0.99)
plt.show()

# Explot graph
imagepath = 'capture.png'
plt.savefig(imagepath)



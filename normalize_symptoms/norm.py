import csv
import pandas as pd
import matplotlib.pyplot as plt

week_meta_info = {}

df = pd.read_csv("symptoms_normalized.csv", skipinitialspace=True)

# DFS of people who have experience 1 week, 2 weeks, 3 weeks etc
week_dfs = []
for i in range(0, 8):
	week_dfs.append(df[df.Numberofweekswithsymptoms >= (i+1)])

i = 0
for i, wdf in enumerate(week_dfs):
	rows_for_csv = []
	header_row = ['Symptom']
	for j in range(1, i+2):
		header_string = 'Week ' + str(j)
		header_row.append(header_string)
	rows_for_csv.append(header_row)
	for column in wdf:
		symptom_by_week = []
		week_meta_info[str(i+1)] = len(wdf[column])
		# IF THE COLUMN IS A SYMPTOM
		if '[' in column:
			if 'Fatigue (Extreme,' in column:
				symptom_by_week.append('[Fatigue (Extreme)]')
			elif 'Fatigue (Moderate' in column:
				symptom_by_week.append('[Fatigue (Moderate)]')
			elif 'Fatigue (Mild' in column:
				symptom_by_week.append('[Fatigue (Mild)]')
			else:
				symptom_by_week.append(str(column))
			#print('Week ', i+1)
			#print('col', column)
			#print('num people:', len(wdf[column]))
			for j in range(1, i+2):
				week_string = 'Week ' + str(j)
				filtered = wdf[(wdf[column].notnull() == True) & (wdf[column].astype(str).str.contains(week_string))]
				symptom_by_week.append(len(filtered))
			rows_for_csv.append(symptom_by_week)

	csvtitle = 'Week_' + str(i+1) + '.csv'
	with open(csvtitle, 'w') as csvfile:
		csvwriter = csv.writer(csvfile, delimiter=',')
		for row in rows_for_csv:
			csvwriter.writerow(row)

print('week_meta_info:')
print(week_meta_info)


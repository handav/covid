import csv
import pandas as pd
import matplotlib.pyplot as plt

week_meta_info = {}

df = pd.read_csv("5_2_roundedup.csv", skipinitialspace=True)
print(df.size)
df = df[(df['COVID-19 Test '].astype(str).str.contains('I tested negative')) | (df['COVID-19 Test '].astype(str).str.contains('I have tested negative'))]

print(df.size)
symptom_text = "What kinds of symptoms have you been experiencing? Use the Week Columns to indicate in which week the symptom first appeared and check additional weeks to indicate how longs the symptoms persisted. For questions regarding severity, consider \"mild\" a 1-5 and \"severe\" a 6-10, on a scale of 10, where 1 is barely noticeable and 10 is needing emergency care. "
symptom_columns = [col for col in df if symptom_text in col or 'Number of weeks sick' in col]
df = df[symptom_columns]
df = df.rename(columns={col: col.split(symptom_text)[1] for col in df.columns if symptom_text in col})

#num_weeks_to_look_at = df['Number of weeks since symptoms started'].max()
num_weeks_to_look_at = 8

# DFS of people who have experience 1 week, 2 weeks, 3 weeks etc
week_dfs = []
for i in range(0, num_weeks_to_look_at):
	week_dfs.append(df[df['Number of weeks sick'] >= (i+1)])

highest_count = 0
i = 0
for i, wdf in enumerate(week_dfs):
	rows_for_csv = []
	header_row = ['Symptom']
	for j in range(1, i+2):
		header_string = 'Week_' + str(j)
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
			elif '(a sensation of burning in your lungs, chest and/or back)' in column:
				symptom_by_week.append(column.split('(a sensation of burning in your lungs, chest and/or back)')[0])
			else:
				symptom_by_week.append(str(column))
			# print('Week ', i+1)
			# print('col', column)
			# print('num people:', len(wdf[column]))
			for j in range(1, i+2):
				week_string = 'Week ' + str(j)
				filtered = wdf[(wdf[column].notnull() == True) & (wdf[column].astype(str).str.contains(week_string))]
				symptom_by_week.append(len(filtered))
				if float(len(filtered))/float(len(wdf[column])) > highest_count:
					highest_count = float(len(filtered))/float(len(wdf[column]))
					print(highest_count, week_string)
			rows_for_csv.append(symptom_by_week)

	csvtitle = 'Week_' + str(i+1) + 'negative_results.csv'
	with open(csvtitle, 'w') as csvfile:
		csvwriter = csv.writer(csvfile, delimiter=',')
		for row in rows_for_csv:
			csvwriter.writerow(row)

print('week_meta_info:')
print(week_meta_info)
print('highest_count_percentage (feel free to take just a few decimals):')
print(highest_count)


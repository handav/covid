import csv
import pandas as pd
import matplotlib.pyplot as plt

# week_meta_info = {}
# week_meta_info_as_list = [638,  635, 620,  585,  523,  387, 203, 84]
# pos_week_meta_info = [148, 148, 141, 131, 116, 80, 29, 14]
# # negative participants
# neg_week_meta_info = [162, 161, 160, 155,  134, 96, 49, 19]


df = pd.read_csv("5_2_withtesting.csv", skipinitialspace=True)
print(df.columns)
symptom_text = "What kinds of symptoms have you been experiencing? Use the Week Columns to indicate in which week the symptom first appeared and check additional weeks to indicate how longs the symptoms persisted. For questions regarding severity, consider \"mild\" a 1-5 and \"severe\" a 6-10, on a scale of 10, where 1 is barely noticeable and 10 is needing emergency care. "
symptom_columns = [col for col in df if symptom_text in col or 'Testing Status' in col]
df = df[symptom_columns]
df = df.rename(columns={col: col.split(symptom_text)[1] for col in df.columns if symptom_text in col})

neg = df[df['Testing Status'].astype(str).str.contains('Negative')]
pos = df[df['Testing Status'].astype(str).str.contains('Positive')]
print(len(pos), len(neg))

header_row = ['Symptom', 'Count', 'Percent', 'Positive Count', 'Positive Percent', 'Negative Count', 'Negative Percent', 'Positive Minus Negative']
rows_for_csv = []
for c in df.columns:
	if '[' in c:
		#print('column', c)
		# for w in range(1, 9):
		# 	print('week', w)
		count = len(df[df[c].notnull()][c])
		percent = round((len(df[df[c].notnull()][c])/638.0)*100.0,1)
		pos_count = len(df[(df[c].notnull()) & (df['Testing Status'].astype(str).str.contains('Positive'))][c])
		pos_percent = round((pos_count/len(pos))*100.0,1)
		neg_count = len(df[(df[c].notnull()) & (df['Testing Status'].astype(str).str.contains('Negative'))][c])
		neg_percent = round((neg_count/len(neg))*100.0,1)
		pos_minus_neg = round(pos_percent-neg_percent, 2)
		# print(count, percent)
		# print(pos_count, pos_percent)
		# print(neg_count, neg_percent)
		# 	#print(df[df[c].astype(str).str.contains(str(w))][c])
		# print('\n')

		rows_for_csv.append([c, count, percent, pos_count, pos_percent, neg_count, neg_percent, pos_minus_neg])

sorted_by_percent = sorted(rows_for_csv,key=lambda x: x[1], reverse=True)

#print(sorted_by_percent)
csvtitle = 'Symptoms_experienced_with_pos_and_neg.csv'
with open(csvtitle, 'w') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter=',')
	csvwriter.writerow(header_row)
	for row in sorted_by_percent:
		csvwriter.writerow(row)

sorted_by_posnegdiff = sorted(rows_for_csv,key=lambda x: x[7], reverse=True)

csvtitle = 'Symptoms_experienced_with_pos_and_neg_sorted.csv'
with open(csvtitle, 'w') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter=',')
	csvwriter.writerow(header_row)
	for row in sorted_by_posnegdiff:
		csvwriter.writerow(row)








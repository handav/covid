# symptoms by weeks 

import pandas as pd
import json

df = pd.read_csv("4_24_responses.csv")
symptoms_to_json = {}

symptom_text = "What kinds of symptoms have you been experiencing? Use the Week Columns to indicate in which week the symptom first appeared and check additional weeks to indicate how longs the symptoms persisted. For questions regarding severity, consider \"mild\" a 1-5 and \"severe\" a 6-10, on a scale of 10, where 1 is barely noticeable and 10 is needing emergency care. "
symptom_columns = [col for col in df if symptom_text in col]
symptoms = df[symptom_columns]
symptoms = symptoms.rename(columns={col: col.split(symptom_text)[1] for col in symptoms.columns if symptom_text in col})

for col in symptoms.columns:
	symptoms_to_json[col] = {
		'num_people_with_this_symptom': symptoms[col].count(),
		'most_common_manifestation_over_weeks': symptoms[col].describe().top,
		'most_common_manifestation_frequency': symptoms[col].describe().freq
	}
	print(symptoms_to_json)



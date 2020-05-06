# partially from https://towardsdatascience.com/very-simple-python-script-for-extracting-most-common-words-from-a-story-1e3570d0b9d0
import csv
import pandas as pd
import collections
import matplotlib.pyplot as plt
#%matplotlib inline

header = []
symptoms = []

# Stopwords
stopwords = set(line.strip() for line in open('stopwords.txt'))
#stopwords = stopwords.union(set(['mr','mrs','one','two','said']))

symptom_row_index = -1
with open('other_symptoms.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile)
	for row in spamreader:
		if len(header) == 0:
			header = row
			for i, h in enumerate(header):
				if 'cleaned_symptoms' in h:
					print(i, h)
					symptom_row_index = i
		if len(row[symptom_row_index]) > 0:
			for symp in row[symptom_row_index].split(','):
				symptoms.append(symp.lower().strip())

#print(symptoms, len(symptoms))



wordcount = {}
# To eliminate duplicates, remember to split by punctuation, and use case demiliters.
for word in symptoms:
    #print(word)
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    word = word.replace("(","")
    word = word.replace(")","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
	#         print(word)
	# print(a)
	# print('\n')

print(len(set(symptoms)))

# Print most common word
n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)



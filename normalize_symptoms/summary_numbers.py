import pandas as pd

df = pd.read_csv('5_2_roundedup.csv', skipinitialspace=True)
recovered = df[df['If you consider yourself to be fully recovered, how many days total was it from onset to full recovery?'].notnull()]

# not_recovered = df[df['If you consider yourself to be fully recovered, how many days total was it from onset to full recovery?'].isnull()]
# cleaned_nr = not_recovered[not_recovered['Number of weeks sick'] >= 0]
# print(len(cleaned_nr))
# print(cleaned_nr['Number of weeks sick'].describe())

recovered = df[df['If you consider yourself to be fully recovered, how many days total was it from onset to full recovery?'] <= 120]

print(len(recovered))
print(recovered['If you consider yourself to be fully recovered, how many days total was it from onset to full recovery?'].describe())
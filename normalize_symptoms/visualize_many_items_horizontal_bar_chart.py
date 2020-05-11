import pandas as pd
import matplotlib.pyplot as plt

pos_neg_diff = pd.read_csv('significant_symptoms_experienced_with_pos_and_neg_sorted.csv')
pos_neg_diff = pos_neg_diff.sort_values(by=['Positive Minus Negative'], ascending=False)

print(pos_neg_diff['Percent'].describe())
pos_neg_diff = pos_neg_diff.set_index('Symptom')
# print(len(pos_neg_diff))
# pos_neg_diff = pos_neg_diff[pos_neg_diff['Percent'] >= 41.5]
# print(len(pos_neg_diff))

# Color for each bar
#cr = [['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red', 'black']]
ax = pos_neg_diff['Positive Minus Negative'].plot(kind='barh', figsize=(12.5,9))
plt.title(label='Symptom Differences Between Positive and Negative Results (bars on the left are more likely for negatively tested respondents and vice versa)', x=-0.2)
ax.set_xlabel('Difference (percentage points)')
ax.set_ylabel('Symptoms')
ttl = ax.title
ttl.set_position([0.1, 1.05])
plt.legend(fontsize='small')
fig = ax.get_figure()
fig.subplots_adjust(left=0.6, right=1.0)
fig.tight_layout()
ax.get_legend().remove()

# Export graph
imagepath = "symptom_pos_neg_diff_common_significant.png"
print(imagepath)
plt.savefig(imagepath)

plt.show()

# pos_neg_diff = pd.read_csv('Symptoms_experienced.csv')
# pos_neg_diff = pos_neg_diff.sort_values(by=['Percent'], ascending=True)

# print(pos_neg_diff['Percent'].describe())
# pos_neg_diff = pos_neg_diff.set_index('Symptom')

# # Color for each bar
# ax = pos_neg_diff['Percent'].plot(kind='barh', figsize=(12,12))
# plt.title(label='Symptoms Experienced At Any Point', x=-0.2)
# ax.set_xlabel('Percentage')
# ax.set_ylabel('Symptoms')
# plt.legend(fontsize='small')
# fig = ax.get_figure()
# fig.subplots_adjust(left=0.3, right=1.0)
# fig.tight_layout()
# ax.get_legend().remove()

# # Export graph
# imagepath = "Symptoms_experienced_overall.png"
# print(imagepath)
# plt.savefig(imagepath)

# plt.show()

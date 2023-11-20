import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'during.csv'
df = pd.read_csv(file_path)

during_study_columns = ['Q1', 'Q2', 'Q3']


percentage_high_responses = (df[during_study_columns] >= 3).mean() * 100

labels_during_study = ['Depend on App', 'Actions Depend on Me', 'What I Did Affects App']

# Bar chart for During Study - Percentage of responses 3 or higher
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(labels_during_study, percentage_high_responses, color=['skyblue', 'dodgerblue', 'royalblue'], alpha=0.8)
ax.set_title('During Study - Percentage of Responses 3 or Higher')
ax.set_ylabel('Percentage')
ax.set_ylim(0, 100)

plt.show()

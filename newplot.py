import matplotlib.pyplot as plt
import pandas as pd


#data_coherence = []

file_path = ''
df = pd.read_csv(file_path)
df_coherence = ['CoherenceOfResponse']

# Plotting
plt.figure(figsize=(8, 6))
df_coherence['CoherenceOfResponse'].value_counts().sort_index().plot(kind='bar', color='lightgreen')
plt.title('Coherence of Response')
plt.xlabel('Response')
plt.ylabel('Frequency')
plt.xticks(rotation=0)  # Rotate x-axis labels if needed
plt.show()

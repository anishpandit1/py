import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file_path = 'during1.csv'
df = pd.read_csv(file_path)

during_study_columns = ['Q1','Q2', 'Q3']

mean_during_study = df[during_study_columns].mean()
std_during_study = df[during_study_columns].std()


labels_during_study = ['Depend on App', 'Actions Depend on Me', 'Felt Good']


fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))

axes[0].bar(labels_during_study, mean_during_study, yerr=std_during_study, capsize=5, color='skyblue', alpha=0.7)
axes[0].set_title('During Study - Mean and Standard Deviation')
axes[0].set_ylim(0, 4)
axes[0].set_yticks(range(5))

plt.tight_layout()
plt.show()

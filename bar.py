import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file_path = 'during.csv'
df = pd.read_csv(file_path)

during_study_columns = ['Something question 1', 'Something 2', 'Something 3']

# Initialize the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

for i, question in enumerate(during_study_columns):
    # Count the percentage of each response for the current question
    response_distribution = df[question].value_counts(normalize=True) * 100
    
    bars = ax.bar(response_distribution.index + i * 0.2, response_distribution, width=0.2,
                  label=f'{question}', alpha=0.8)

    # Annotate each bar with its percentage value
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}%', 
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

# Set common labels and legend
ax.set_title('During Study - Distribution of Responses')
ax.set_xlabel('Response')
ax.set_ylabel('Percentage')
ax.set_ylim(0, 100)
ax.legend(title='Question', loc='upper left')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()

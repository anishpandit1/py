import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


file_path = 'Book2.csv'
data = pd.read_csv(file_path)

combined_data = pd.concat([data['Indicator1'], data['Indicator2']], axis=0) # 2 indicators with different temperature value.

# Create a countplot using seaborn
plt.figure(figsize=(8, 6))
sns.countplot(x=combined_data, hue=combined_data.index % 2, palette='Blues')  # Use 'hue' to distinguish between Indicator1 and Indicator2

plt.title('Frequency of Responses in Sessions 1/2/3 and 7/8/9')
plt.xlabel('Responses')
plt.ylabel('Frequency')
plt.legend(title='Session')
plt.show()

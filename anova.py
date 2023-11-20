import pandas as pd
from scipy.stats import f_oneway

# Load CSV file into a DataFrame
file_path = 'during.csv'
df = pd.read_csv(file_path)

# Select relevant columns for analysis
during_study_columns = ['Question1', 'Q2', 'Q3']

# Perform ANOVA
anova_results = f_oneway(df[during_study_columns[0]], df[during_study_columns[1]], df[during_study_columns[2]])

# Print ANOVA results
print("ANOVA Results:")
print("F-statistic:", anova_results.statistic)
print("P-value:", anova_results.pvalue)

# Interpret the results
alpha = 0.05
if anova_results.pvalue < alpha:
    print("The differences between at least two groups are statistically significant.")
else:
    print("There is no significant difference between the groups.")

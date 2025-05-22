# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Load the Excel file into a pandas DataFrame.
# 'header=0' indicates that the first row (row 0) contains the column names.
df = pd.read_excel('DATA_Kiss_count_gender_and_IQ.xlsx', header=0)


###### Divide IQ into 2 quantile-based groups (Low and High) ######
# Also return the bin edges to use for labeling the IQ ranges
df['IQ Level'] = pd.qcut(df['IQ'], q=2, labels=['Low', 'High'])

### Compute the Pearson correlation coefficient and p-value ######
# between IQ and Age of First Kiss
r_value, p_value = pearsonr(df['IQ'], df['Age of First Kiss'])

# Plot scatter points colored by IQ Level
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x='IQ',
    y='Age of First Kiss',
    hue='IQ Level',
    palette={'Low': 'lightgreen', 'High': 'orange'},
    alpha=0.6,
    edgecolor='gray'
)

# Add single regression line 
sns.regplot(
    data=df,
    x='IQ',
    y='Age of First Kiss',
    scatter=False,
    color='gray',
    line_kws={'linewidth': 2}
)

# Title includes correlation info
plt.title(
    f'IQ vs Age of First Kiss\n r = {r_value:.2f}, p = {p_value:.3f}',
    fontsize=14
)

# Axis labels
plt.xlabel('IQ', fontsize=12)
plt.ylabel('Age of First Kiss', fontsize=12)

# Grid and layout
plt.grid(True)
plt.tight_layout()
plt.show()

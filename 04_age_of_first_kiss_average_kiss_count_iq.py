# -*- coding: utf-8 -*-
"""04_Age of First Kiss_Average Kiss Count_IQ

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11GpR5yEvzQhLkUKCKCZYNkdz-9BjDm17
"""

# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


# Load the Excel file into a pandas DataFrame.
# 'header=0' indicates that the first row (row 0) contains the column names.
df = pd.read_excel('DATA_Kiss_count_gender_and_IQ.xlsx', header=0)

# Step 1: Divide IQ into 2 groups (Low and High) using quantile-based binning
df['IQ Level'] = pd.qcut(df['IQ'], q=2, labels=['Low', 'High'])

# Step 2: Group data by IQ Level and Age of First Kiss, and calculate average Kiss Count
line_df = df.groupby(['IQ Level', 'Age of First Kiss'], observed=True)['Kiss Count'].mean().reset_index()

# Step 3: Plot a line chart showing average Kiss Count vs Age of First Kiss by IQ Level
plt.figure(figsize=(10, 6))
sns.lineplot(
    data=line_df,                    # The pre-processed data
    x='Age of First Kiss',           # X-axis: age at first kiss
    y='Kiss Count',                  # Y-axis: average number of kisses
    hue='IQ Level',                  # Line color based on IQ Level
    palette='Set2',                  # A soft color
    marker='o'                       # Add markers to line plot
)

# Step 4: Customize the plot with title, axis labels, grid, and legend
plt.title('Average Kiss Count vs Age of First Kiss by IQ Level')
plt.xlabel('Age of First Kiss')
plt.ylabel('Average Kiss Count')
plt.grid(True)
plt.legend(title='IQ Level')        # Legend with title

plt.tight_layout()
plt.show()
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Load the Excel file into a pandas DataFrame.
# 'header=0' indicates that the first row (row 0) contains the column names.
df = pd.read_excel('DATA_Kiss_count_gender_and_IQ.xlsx', header=0)

# Display the first 20 rows of the DataFrame to preview the data.
print("df_head",df.head(20))

# Show the list of column names in the DataFrame.
# Useful for checking the exact spelling and structure of the dataset's columns.
print("df_index",df.columns)

# Convert gender to binary: 0 for female, 1 for male (for correlation analysis)
df['Gender_binary'] = df['Gender'].map({'female': 0, 'male': 1})

# Calculate Pearson correlation coefficient and p-value between gender and age of first kiss
r_value, p_value = pearsonr(df['Gender_binary'], df['Age of First Kiss'])

# Get sorted unique ages for consistent plotting
age_bins = sorted(df['Age of First Kiss'].unique())

# Count the number of males and females for each age
male_counts = df[df['Gender'] == 'male']['Age of First Kiss'].value_counts().reindex(age_bins, fill_value=0)
female_counts = df[df['Gender'] == 'female']['Age of First Kiss'].value_counts().reindex(age_bins, fill_value=0)

# Create horizontal bar plot (pyramid-style)
plt.figure(figsize=(10, 6))
plt.barh(age_bins, -male_counts, color='lightblue', label='Male')       # Male counts (plotted to the left)
plt.barh(age_bins, female_counts, color='lightpink', label='Female')    # Female counts (plotted to the right)

# Axis labels and title with r and p values
plt.xlabel('Number of People')
plt.ylabel('Age of First Kiss')
plt.title(f'Age of First Kiss Distribution by Gender\nr = {r_value:.2f}, p = {p_value:.3f}')
plt.legend(loc='upper right')

# Set y-axis ticks to show each age
plt.yticks(ticks=age_bins)

# Convert x-axis labels to absolute values so they appear positive
xticks = plt.xticks()[0]
plt.xticks(ticks=xticks, labels=[abs(int(x)) for x in xticks])

# Add light grid lines on the x-axis
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Optimize layout
plt.tight_layout()
plt.show()
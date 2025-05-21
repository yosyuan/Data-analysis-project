# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import pandas as pd

# Load the Excel file into a pandas DataFrame.
# 'header=0' indicates that the first row (row 0) contains the column names.
df = pd.read_excel('DATA_Kiss_count_gender_and_IQ.xlsx', header=0)

# Calculate the Pearson correlation coefficient and p-value between Kiss Count and Age of First Kiss
r_value, p_value = pearsonr(df['Kiss Count'], df['Age of First Kiss'])

# Create a scatter plot with a linear regression line
sns.lmplot(
    x='Kiss Count',                      # X-axis: total number of people kissed
    y='Age of First Kiss',               # Y-axis: age when the participant had their first kiss
    data=df,
    scatter_kws={'alpha': 0.6},          # Transparency of the scatter points
    line_kws={'color': 'red'}            # Color of the regression line
)


# Add a title with the correlation coefficient and p-value
plt.title(f'Relationship between Kiss Count and Age of First Kiss\nr = {r_value:.2f}, p = {p_value:.3f}')

# Label the axes
plt.xlabel('Kiss Count')
plt.ylabel('Age of First Kiss')

# Optimize layout
plt.tight_layout()
plt.show()
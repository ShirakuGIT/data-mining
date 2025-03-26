# Note: pip install scipy

from scipy.stats import chi2_contingency, pearsonr

# Chi-Square Test
observed = [
    [10, 20, 30],  # Row 1
    [6,  9,  17]   # Row 2
]
chi2, p, dof, expected = chi2_contingency(observed)
print("Chi-Square Statistic:", chi2)
print("P-Value:", p)

# Pearson Correlation Coefficient
x = [10, 20, 30, 40, 50]
y = [15, 25, 35, 45, 55]
correlation, p_value = pearsonr(x, y)
print("Pearson Correlation Coefficient:", correlation)
print("P-Value:", p_value)

# NOTE: Install mlxtend
# pip install mlxtend

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import pandas as pd

# Example transaction data
data = {'milk': [1, 1, 1, 0, 1],
        'bread': [1, 1, 0, 1, 1],
        'eggs': [1, 0, 1, 1, 1],
        'butter': [0, 0, 0, 0, 1]}

df = pd.DataFrame(data)

# Find frequent itemsets
frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)
print("Frequent Itemsets:")
print(frequent_itemsets)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
print("\nAssociation Rules:")
print(rules)

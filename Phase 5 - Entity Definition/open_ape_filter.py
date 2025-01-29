import os
import pandas as pd

ape_path = '../Phase 2 - Information Gathering/DataCleaning/open_ape_clean.csv'
output_path = '../Data/open_ape_filtered.csv'
ape_df = pd.read_csv(ape_path, encoding='ISO-8859-1')


# Group by Stazione and Inquinante, take first 50 rows of each group, then reset index
filtered_ape_df = ape_df.groupby(['Municipality']).head(20).reset_index(drop=True)

# Round the float values to 2 decimal places
filtered_ape_df = filtered_ape_df.round(2)

# Add an incremental ID
filtered_ape_df['ID'] = range(1, len(filtered_ape_df) + 1)

print(len(filtered_ape_df))

filtered_ape_df.to_csv(output_path, index=False)

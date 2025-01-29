import os
import pandas as pd

pollution_path = '../Data/pollution.csv'
output_path = '../Data/pollution_filtered.csv'
pollution_df = pd.read_csv(pollution_path, encoding='ISO-8859-1')


# Group by Stazione and Inquinante, take first 50 rows of each group, then reset index
filtered_pollution_df = pollution_df.groupby(['Stazione', 'Inquinante']).head(100).reset_index(drop=True)

print(filtered_pollution_df.head())

filtered_pollution_df.to_csv(output_path, index=False)

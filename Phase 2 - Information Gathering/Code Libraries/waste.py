import pandas as pd

waste_diff_file = '../../Data/waste_differentiated.csv'
waste_undiff_file = '../../Data/waste_undifferentiated.csv'

diff_df = pd.read_csv(waste_diff_file, sep=',', encoding='utf-8')
undiff_df = pd.read_csv(waste_undiff_file, sep=',', encoding='utf-8')

# Concatenate the two dataframes adding a column type to differentiate them
diff_df['Type'] = 'Differentiated'
undiff_df['Type'] = 'Undifferentiated'

# Merge the two dataframes
merged_df = pd.concat([diff_df, undiff_df])

# Filter the columns to only the ones needed
merged_df = merged_df[[
    '_id', 'anno', 'codEnte', 'valore', 'Type'
]]

# Rename the columns to be more descriptive
merged_df = merged_df.rename(columns={
    '_id': 'ID', 'anno': 'Year', 'codEnte': 'Waste Comapny Code', 'valsore': 'Value'
})

# Save the merged data to a new file
output_file = '../DataCleaning/waste_clean.csv'
merged_df.to_csv(output_file, index=False, encoding='utf-8')
print(f'File saved as {output_file}')
import pandas as pd

opendata_file = '../../Data/open_ape.csv'
istat_file = '../../Data/istat.csv'

opendata_df = pd.read_csv(opendata_file, sep='\t', encoding='utf-8')
istat_df = pd.read_csv(istat_file, sep=';', encoding='ISO-8859-1')

# Filter the ISTAT data to only the columns needed
istat_df = istat_df[['Codice Comune formato numerico', 'Denominazione in italiano']]

# Rename the columns to match the OpenData file
opendata_df = opendata_df.rename(columns={'c_istat': 'Codice Comune formato numerico'})
merged_df = opendata_df.merge(istat_df, on='Codice Comune formato numerico', how='inner')

# Filter the columns to only the ones needed
merged_df = merged_df[[
    'Denominazione in italiano', 'Codice Comune formato numerico', 'c_cat', 'anno_costruzione', 'zona_climatica', 
    'energia_invernale', 'energia_sanitaria', 'energia_globale_ubicazione', 'epglnren', 'epglren',
    'gradi_giorno', 'emissioneco2', 
]]

# Rename the columns to be more descriptive
merged_df = merged_df.rename(columns={
    'Denominazione in italiano': 'Comune', 'Codice Comune formato numerico': 'Codice ISTAT', 'c_cat': 'Codice Catastale',
    'anno_costruzione': 'Anno Costruzione', 'zona_climatica': 'Zona Climatica',
    'energia_invernale': 'Energia Invernale', 'energia_sanitaria': 'Energia Sanitaria',
    'energia_globale_ubicazione': 'Energia Globale Ubicazione', 'epglnren': 'Prestazione Energetica Globale Non Rinnovabile',
    'epglren': 'Prestazione Energetica Globale Rinnovabile', 'gradi_giorno': 'Gradi Giorno', 'emissioneco2': 'Emissione CO2',
})

# Save the merged data to a new file
output_file = '../DataCleaning/open_ape_clean.csv'
merged_df.to_csv(output_file, index=False, encoding='utf-8')
print(f'File saved as {output_file}')

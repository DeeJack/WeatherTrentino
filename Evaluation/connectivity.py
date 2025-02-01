import pandas
import os

base_path = os.path.split(os.path.dirname(__file__))[0]

def openape_connectivity(open_ape_path: str):
    open_ape = pandas.read_csv(open_ape_path)
    self_connectivity(open_ape.shape)

    # Count rows where a specific column is not null
    non_null_count = open_ape['Municipality'].count()  # Replace 'column_name' with your desired column
    print(f"Consumption x Location: {non_null_count}")
    
def self_connectivity(shape: tuple):
    n_rows = shape[0]
    n_cols = shape[1]
    print(f'N rows: {n_rows}, n cols: {n_cols}, res: {n_rows * n_cols}')
    
if __name__ == '__main__':
    open_ape_path = os.path.join(base_path, 'Phase 2 - Information Gathering', 'DataCleaning', 'open_ape_filtered.csv')
    waste_path = os.path.join(base_path, 'Phase 2 - Information Gathering', 'DataCleaning', 'waste.csv')
    pollution_path = os.path.join(base_path, 'Phase 2 - Information Gathering', 'DataCleaning', 'pollution_filtered.csv')
    air_path = os.path.join(base_path, 'Data', 'air_quality.csv')
    demo_path = os.path.join(base_path, 'Data', 'trentino_demographic.csv')
    
    openape_connectivity(open_ape_path)
    
    paths = [waste_path, pollution_path, air_path, demo_path]
    for path in paths:
        print(f'Path: {path}')
        self_connectivity(pandas.read_csv(path).shape)
        
    location_path = os.path.join(base_path, 'Data', 'location.json')
    location = pandas.read_json(location_path)
    print(f'Location')
    self_connectivity(location.shape)
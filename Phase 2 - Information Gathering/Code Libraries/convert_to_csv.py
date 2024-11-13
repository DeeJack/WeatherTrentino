import json

FILES = [
    '../../Data/air_quality.json',
    '../../Data/waste_differentiated.json',
    '../../Data/waste_undifferentiated.json',
    '../../Data/waste_differentiated_2019.json'
]

for file in FILES:
    with open(file, 'r') as f:
        data = json.load(f)
        
        with open(file.replace('.json', '.csv'), 'w') as f:
            fields = []
            for field in data['result']['fields']:
                fields.append(field['id'])
                f.write(field['id'] + ',')
            f.write('\n')
            for record in data['result']['records']:
                for field in fields:
                    f.write(str(record[field]) + ',')
                f.write('\n')
import requests
import json
from time import sleep

RESOURCE_IDS = [
    '0618e969-678a-47c0-a467-3d59cd272bc0', # Undifferentiated waste
    '49032652-b64e-410f-b1da-6673ea434ec5', # Differentiated waste
    'c07a80cc-d471-49fa-bc76-fd6b41f60f88', # Air Quality
]

url = 'https://dati.trentino.it/api/action/datastore_search?resource_id='

for resource_id in RESOURCE_IDS:
    url += resource_id + '&limit=9999'

    response = requests.get(url)
    if response.status_code != 200:
        print(f'Error: {response.status_code}')
        continue
    object = json.loads(response.text)
    with open(f'../../Data/{resource_id}.json', 'w') as f:
        json.dump(object, f)
    sleep(1)

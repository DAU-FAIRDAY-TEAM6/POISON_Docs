import json
import csv

data = []
with open('./json_data/business.json', 'r', encoding='UTF8') as f:
    lines = f.readlines()
    for i in lines:
        json_data = json.loads(i.strip())
        # if json_data.get('city', "null") != "Philadelphia":
        #     continue
        data.append(json_data)

print(f'data 크기: {len(data)}')

with open('./csv_data/business.csv', 'w', newline='', encoding='UTF8') as csvfile:
    fieldnames = ['business_id', 'name', 'address', 'city', 'latitude', 'longitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for entry in data:
        address = entry['address']
        cleaned_address = address.replace("'", "").replace('"', '').replace(',', '') # , 제거
        writer.writerow({
            'business_id': entry['business_id'],
            'name': entry['name'].replace("'", "").replace('"', '').replace(',', ''),
            'address': entry['address'].replace("'", "").replace('"', '').replace(',', ''),
            'city': entry['city'].replace("'", "").replace('"', '').replace(',', ''),
            'latitude': entry['latitude'],
            'longitude': entry['longitude']
        })



import json
import csv

data = []

with open('./json_data/user.json', 'r', encoding='UTF8') as f:
    lines = f.readlines()
    for i in lines:
        json_data = json.loads(i)
        data.append(json_data)
        if(json_data['user_id']) == "user_id: lzpM_Vf2rKA4ivGtAIOH4w":
            print("찾음")

print(f'data 크기: {len(data)}')

# with open('./csv_data/user.csv', 'w', newline='', encoding='UTF8') as csvfile:
#     fieldnames = ['user_id', 'name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     for entry in data:
#         writer.writerow({
#             'user_id': entry['user_id'],
#             'name': entry['name']
#         })
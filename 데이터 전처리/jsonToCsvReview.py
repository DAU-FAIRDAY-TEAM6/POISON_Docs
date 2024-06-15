import json
import csv
import time
start_time = time.time()  # 시작 시간 기록

# Philadelphia POI의 Id를 담는 set 생성
# Philadelphia POI의 review만 골라 csv 생성


data = []
business_ids_set = set()  # business_id를 담을 set
user_ids_set = set()  # user_id를 담을 set

# POI의 businessId를 담는 set 생성
with open('./csv_data/business.csv', 'r', encoding='UTF8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        business_ids_set.add(row['business_id'])
print(f'business_ids_set 크기: {len(business_ids_set)}')

# User의 user_id를 담는 set 생성
with open('./csv_data/user.csv', 'r', encoding='UTF8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        user_ids_set.add(row['user_id'])
print(f'user_ids_set 크기: {len(user_ids_set)}')

with open('./json_data/review.json', 'r', encoding='UTF8') as f:
    lines = f.readlines()
    print(f'review 전체 데이터 크기: {len(lines)}')
    for index, i in enumerate(lines):
        # if index > 20000:
        #     break
        json_data = json.loads(i)
        if json_data.get('business_id', "-1") in business_ids_set and json_data.get('user_id', '-1') in user_ids_set:
            data.append(json_data)

# CSV 파일 열기
with open('./bumku/review.csv', newline='', encoding='utf-8') as csvfile:
    # CSV 파일 읽기
    csv_reader = csv.reader(csvfile)
    
    # CSV 파일에서 10줄 읽기
    for i, row in enumerate(csv_reader):
        data.append(i)

print(f'data 크기: {len(data)}')

with open('./bumku/review.csv', 'w', newline='', encoding='UTF8') as csvfile:
    # fieldnames = ['review_id', 'user_id', 'business_id', 'stars', 'text']
    fieldnames = ['review_id', 'text']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for index, entry in enumerate(data):
        writer.writerow({
            'review_id': entry['review_id'],
            # 'user_id': entry['user_id'],
            # 'business_id': entry['business_id'],
            # 'stars': entry['stars'],
            'text': entry['text'].replace("'", "").replace('"', '').replace(',', '').replace("\n", " ")
        })

end_time = time.time()  # 종료 시간 기록
print(f'데이터 처리 및 CSV 파일 생성에 소요된 시간: {end_time - start_time} 초')
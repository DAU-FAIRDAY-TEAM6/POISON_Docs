import pandas as pd
import json
import time

start_time = time.time()  # 시작 시간 기록

# Philadelphia POI의 Id를 담는 set 생성
# Philadelphia POI의 review만 골라 csv 생성

# POI의 businessId를 담는 set 생성
business_df = pd.read_csv('./csv_data/business.csv')
business_ids_set = set(business_df['business_id'])

print(f'business_ids_set 크기: {len(business_ids_set)}')

# User의 user_id를 담는 set 생성
user_df = pd.read_csv('./csv_data/user.csv')
user_ids_set = set(user_df['user_id'])

print(f'user_ids_set 크기: {len(user_ids_set)}')

data = []
with open('./json_data/review.json', 'r', encoding='UTF8') as f:
    for line in f:
        json_data = json.loads(line)
        if json_data.get('business_id', "-1") in business_ids_set and json_data.get('user_id', '-1') in user_ids_set:
            data.append(json_data)

print(f'review 전체 데이터 크기: {len(data)}')

df = pd.DataFrame(data)
df = df[['review_id', 'text']]

df['text'] = df['text'].str.replace("'", "").str.replace('"', '').str.replace(',', '').str.replace("\n", " ")

df.to_csv('./bumku/review2.csv', index=False, encoding='UTF8')

end_time = time.time()  # 종료 시간 기록
print(f'데이터 처리 및 CSV 파일 생성에 소요된 시간: {end_time - start_time} 초')
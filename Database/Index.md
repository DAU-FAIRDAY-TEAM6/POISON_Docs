## 1. 인덱스란?
인덱스란 추가적인 쓰기 작업과 저장 공간을 활용하여 데이터베이스 테이블의 검색 속도를 향상시키기 위한 자료구조이다.

만약 우리가 책에서 원하는 내용을 찾는다고 하면, 책의 모든 페이지를 찾아 보는것은 오랜 시간이 걸린다. 그렇기 때문에 책의 저자들은 책의 맨 앞 또는 맨 뒤에 색인을 추가하는데, 데이터베이스의 index는 책의 색인과 같다.

데이터베이스에서도 테이블의 모든 데이터를 검색하면 시간이 오래 걸리기 때문에 데이터와 데이터의 위치를 포함한 자료구조를 생성하여 빠르게 조회할 수 있도록 돕고 있다.

![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/52cbfbe1-51c1-43d0-b5b8-9bfd8224b6e1)


장점 
1. 검색 대상 레코드의 범위를 줄여 검색 속도를 빠르게 할 수 있다.

2. 중복 데이터를 방지하거나 특정 컬럼의 유일성(Unique)을 보장할 수 있다.

3. ORDER BY 절과 GROUP BY 절, WHERE 절 등이 사용되는 작업이 더욱 효율적으로 처리된다.

 

단점
1. 인덱스 생성에 따른 추가적인 저장 공간이 필요하다. (인덱스 사용 시 해당 정보를 담은 MYI 파일 생성)

2. CREATE(삽입), DELETE(삭제), UPDATE(수정) 작업 시에도 인덱스를 업데이트해야 하므로 성능 저하가  발생할 수 있다.

3. 한 페이지를 동시에 수정할 수 있는 병행성이 줄어든다.

4. 인덱스 생성 시간이 오래 걸릴 수 있다.


인덱스는 데이터베이스에서 검색 및 처리하는 속도를 향상시키는 데 중요한 역할을 한다.

하지만, 인덱스를 적절하게 활용하지 않으면 오히려 데이터베이스의 성능이 저하되거나 저장 공간이 낭비될 수 있다.

 

따라서, 상황에 맞게 인덱스를 적절히 선택하고 생성하는 것이 가장 중요하다.

<br><br><br><br>

## 2. 인덱스의 자료구조
인덱스를 구현하기 위해서는 다양한 자료구조를 사용할 수 있는데, 가장 대표적인 해시 테이블과 B+Tree에 대해서 알아보자. 

 

- 해시 테이블(Hash Table)
해시 테이블은 (Key, Value)로 데이터를 저장하는 자료구조 중 하나로 빠른 데이터 검색이 필요할 때 유용하다. 해시 테이블은 Key값을 이용해 고유한 index를 생성하여 그 index에 저장된 값을 꺼내오는 구조이다.


![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/9b32ce2d-9856-4f86-aa89-4d30a9fbd61d)


해시 테이블 기반의 DB 인덱스는 (데이터=컬럼의 값, 데이터의 위치)를 (Key, Value)로 사용하여 컬럼의 값으로 생성된 해시를 통해 인덱스를 구현하였다. 해시 테이블의 시간복잡도는 O(1)이며 매우 빠른 검색을 지원한다.

하지만 DB 인덱스에서 해시 테이블이 사용되는 경우는 제한적인데, 그러한 이유는 해시가 등호(=) 연산에만 특화되었기 때문이다. 해시 함수는 값이 1이라도 달라지면 완전히 다른 해시 값을 생성하는데, 이러한 특성에 의해 부등호 연산(>, <)이 자주 사용되는 데이터베이스 검색을 위해서는 해시 테이블이 적합하지 않다.

<br><br>

### B+ Tree
B+Tree는 DB의 인덱스를 위해 자식 노드가 2개 이상인 B-Tree를 개선시킨 자료구조이다.

가장 하단의 leaf node를 보면 같은 레벨의 노드들끼리 서로 linked list 형식으로 연결되어 있다. 시퀀셜 액세스를 효과적으로 처리하기 위해 key : value의 페이지는 leaf node에만 존재하고, 그 외 레벨의 node들은 오직 인덱싱을 위한 key를 저장하는 용도로만 사용된다.

![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/333d8d8e-3b3b-4f1f-93ca-5b1c204a3e1d)


특징

- 리프노드(데이터노드)만 인덱스와 함께 데이터(Value)를 가지고 있고, 나머지 노드(인덱스노드)들은 데이터를 위한 인덱스(Key)만을 갖는다. 
- 리프노드들은 LinkedList로 연결되어 있다. 
- 데이터 노드 크기는 인덱스 노드의 크기와 같지 않아도 된다.

<br><br><br><br>

## 3. 클러스터링 인덱스 vs 논-클러스터링 인덱스

클러스터링 인덱스와 논-클러스터링 인덱스는 아래 사진과 같이 예시를 들 수 있다. 

![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/54f1011c-1dcc-466a-b66f-d1ad89af4399)

우리는 따로 인덱스를 걸지 않아도 자연스럽게 index를 사용하고 있었다. 

```
CREATE TABLE member (
    id		int		--> primary key
    name	varchar(255),
    email	varchar(255)	--> unique
);
```

위와 같은 테이블이 있을 때 인덱스는 몇 개 일까?? 총 2개의 인덱스를 사용하고 있다. primary key 가 적용된 id는 클러스터링 인덱스, unique key 가 적용된 email 은 논-클러스터링 인덱스가 젹용되어있다. 

<br><br>

### 클러스터링 인덱스

위에서 만든 table에 어떠한 제약조건을 걸지 않고 순차적으로 데이터를 넣는다고 가정해보자. 

데이터를 넣은 순서대로 테이블에 데이터가 쌓일 것이다. 

![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/fad534f5-c4cf-4d04-999c-2af9355a6940)

여기서 클러스터링 인덱스를 적용해보자. 아래 두 가지 방법 모두 클러스터링 인덱스를 걸 수 있다. 

```
ALTER TABLE member ADD CONSTRAINT pk_id PRIMARY KEY (id);
```


```
ALTER TABLE member MODIFY COLUMN id int NOT NULL;
ALTER TABLE member ADD CONSTRAINT nuq_id UNIQUE (id);
```

- 인덱스 적용 후

![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/a64b9b15-4445-46aa-b5de-22e6165727ec)


**특징**

- 실제 데이터 자체가 정렬
- 테이블당 1개만 존재 가능
- 리프 페이지가 데이터 페이지
- 아래의 제약조건 시 자동 생성
 - primary key (우선순위)
 - unique + not null

<br><br>

### 논-클러스터링 인덱스

마찬가지로 정렬되어있지 않은 데이터에 name으로 논-클러스터링 인덱스를 걸어보자. 

![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/78113ba8-f82b-4373-b385-5781a7299399)

아래 세 가지 방법 모두 클러스터링 인덱스를 걸 수 있다. 

```
ALTER TABLE member ADD CONSTRAINT unq_name UNIQUE (name);
 
CREATE UNIQUE INDEX unq_idx_name ON member (name);
 
CREATE INDEX idx_name ON member (name);
```

- 인덱스 적용 후

![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/acb37495-0ccd-4fb0-92ea-94c793f4b893)

**특징**

- 실제 데이터 페이지는 그대로 존재
- 별도의 인덱스 페이지 생성 => 추가 공간 필요
- 테이블당 여러 개 존재
- 리프 페이지에 실제 데이터 페이지 주소를 담고 있음
- 아래의 제약조건 시 자동 생성
 - uinique 제약 조건 적용 시 자동 생성
 - 직접 index 생성 시 논-클러스터링 인덱스 생성

<br><br><br><br>

## 4. 클러스터링 인덱스와 논-클러스터링 인덱스를 함께 적용
클러스터링 인덱스와 논-클러스터링 인덱스를 함께 적용하면 어떻게 될까??

 

id 컬럼에 클러스터링 인덱스 + name 컬럼에 논클러스터링 인덱스 를 적용하고 테이블 구조를 살펴보자.

![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/75ee57b5-f416-4f92-94f2-a8a1717d04d4)


만약 name = '라라' 로 데이터를 조회한다면 논-클러스터링 인덱스 페이지를 타고 라라의 index 값을 얻게 된다. 찾은 index 값으로 클러스터링 인덱스 페이지를 조회하여 실제 데이터에 접근할 수 있다. 

 

이전과 달리 논-클러스터링 인덱스의 리프 페이지에선 실제 데이터가 저장된 주소를 가르키지 않는다. 

 

왜 그럴까??

 

이유는 새로운 데이터가 insert 될 때 추가적인 작업들이 많아지기 때문이다. 

만약 "파랑" 이라는 이름을 가진 데이터가 새로 추가된다면 1000번째 주소를 가진 페이지에 데이터가 들어가게 될 것이다. 그러면 페이지 분할이 발생할 것이고 name 컬럼의 리프 페이지의 주소도 변경해줘야 한다. 

<br><br><br><br>

## 5. 인덱스 적용 기준
인덱스를 적용하는 기준에 대해 살펴보자. 

- 사용하면 좋은 경우
1. 카디널리티가 높은 (중복도가 낮은) 컬럼
2. where, join, order by 절에 자주 사용되는 컬럼
3. insert, update, delete 가 자주 발생하지 않는 컬럼
4. 규모가 작지 않은 테이블


```
카디널리티란?
중복도가 ‘낮으면’ 카디널리티가 ‘높다’고 표현한다.

중복도가 ‘높으면’ 카디널리티가 ‘낮다’고 표현한다.

카디널리티는 전체 행에 대한 특정 컬럼의 중복 수치를 나타내는 지표이다.
```

아래 테이블의 각 카디널리티를 살펴보면 다음과 같다.


![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/89bec388-2fd6-4147-a320-93e39bbb0f1b)


여기서는 ID, 이름, 이메일 등이 좋은 인덱스가 될 수 있다. 


## 6. 인덱스 성능 비교
![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/ea703ba6-d596-4c49-887b-01825e9429c8)
![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/89e20bf7-a266-4108-ab69-b0019e017d0d)



Ref)
<br>
https://www.youtube.com/watch?v=edpYzFgHbqs
<br>
https://ittrue.tistory.com/331

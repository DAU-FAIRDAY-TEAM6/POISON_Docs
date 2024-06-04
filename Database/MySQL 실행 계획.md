## 1. 실행 계획
실행 계획도 정말 여러가지가 있지만 가장 중요하고 많이 나오는 3가지는 다음과 같다.

- all: 테이블 전체를 스캔

![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/cc1a3fc8-e905-41d0-8dc6-b69d753dadd4)

full table scan을 의미한다. full table scan을 하는 경우는 두가지가 있다.  

 

1. 인덱스가 없어서 full table scan 하는 경우

2. 인덱스가 있지만 full table scan 하는 경우

 

두번째 경우는 의아할수도 있지만

인덱스가 있지만 데이터 전체의 개수가 얼마되지 않거나

인덱스가 있지만 읽고자 하는 데이터가 25%가 넘어간다면 full table scan이 일어난다. 

- range: 인덱스를 이용하여 범위 검색을 할 때

![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/8449d549-825e-4975-a548-543c1b5ceb95)

이상적으로 인덱스를 잘 걸었을 때 나타나는 실행 계획이다. 필요한 부분만 데이터를 읽기 때문에 disk io를 줄일 수 있다. 

 <br><br>

- index: 인덱스 전체를 스캔할 때

![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/99f8d9c6-9e04-4266-8e70-4e309eda332e)

실행 계획 all 과 유사하지만 data를 다 읽는것이 아닌 index를 전부 읽는 것이다.

index는 데이터보단 파일 크기가 작기 때문에 full table scan보단 성능이 우수하고, 당연히 range scan보다는 성능이 좋지 못하다.

<br><br><br><br>

## 2.1 인덱스 적용 사례

아래 사진과 같은 테이블이 있을 때 어느 컬럼에 인덱스를 걸어야할까??

![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/238e7cd9-efea-4f6b-b8f1-7369133bdefe)

이전 index 게시글에도 나와있었지만 아래 두가지 정도로 기준을 정할 수 있다. 

 

1. 카디널리티가 높은 컬럼에 대해 인덱스를 생성

2. 서비스의 특성상 무엇에 대한 조회가 많이 일어나는지 파악

 

nickname에 대한 조회가 많이 일어나고 nickname 컬럼의 카디널리티 또한 높다고 가정하고 진행하겠다.  

- 더미데이터 insert
실험에 앞서 dummy data를 넣어줘야한다. 

나같은 경우 mysql workbench를 통해 sql문을 실행시켜 10만건의 데이터를 넣어주었다. 

```
DELIMITER $$
DROP PROCEDURE IF EXISTS loopInsert$$
 
CREATE PROCEDURE loopInsert()
BEGIN
    DECLARE i INT DEFAULT 1;
        
    WHILE i <= 100000 DO
        INSERT INTO crew(id, nickname, track, age)
          VALUES(i, concat('dgjinsu',i), 'backend', FLOOR(RAND() * 11) + 20);
        SET i = i + 1;
    END WHILE;
END$$
DELIMITER $$
 
 
CALL loopInsert;
```


![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/6d8a4a95-cdce-4ae4-abc7-3888d8fce978)

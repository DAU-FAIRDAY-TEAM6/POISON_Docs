## Replication 진행 목적
AI 모델 재학습 시 User, POI, Review의 전체 레코드를 탐색하게된다. 데이터가 900만건이 넘기 때문에 질의 시간이 오래 걸렸고 다른 요청을 처리하는 데 문제가 발생할 것이라 판단했다. 
따라서 MySQL Replication을 사용하여 Master-Slave 관계의 DB를 구축하고 Transaction 타입에 따라 DB에 접근하게 함으로써 부하를 분산시키려 한다. 


## 복제(Replication)
복제(Replication)는 1개 이상의 레플리카(replica) 저장소가 소스 저장소와 동기화를 자동으로 유지하는 과정이다. 사용하기 위한 최소 구성은 Master / Slave이다.
<br><br>
Master DBMS 역할
웹서버로 부터 데이터 등록/수정/삭제 요청시 바이너리로그(Binarylog)를 생성하여 Slave 서버로 전달하게 된다. (웹서버로 부터 요청한 데이터 등록/수정/삭제 기능을 하는 DBMS로 많이 사용)
<br><br>
Slave DBMS 역할
Master DBMS로 부터 전달받은 바이너리로그(Binarylog)를 데이터로 반영하게 된다. (웹서버로 부터 요청을 통해 데이터를 불러오는 DBMS로 많이 사용)
<br><br>
<br><br>
<br><br>

## MySQL Replication 사용 목적
mysql 리플리케이션의 사용목적은 크게 실시간 Data 백업과 여러대의 DB 서버의 부하를 분산시킬 수 있다. 

 
먼저 데이터의 백업이다.


예를 들어 Master 서버를 데이터의 원본서버, Slave 서버를 백업 서버로 지칭하였다.


Master 서버에 DBMS의 등록/수정/업데이트가 생기는 즉시 Slave 서버의 변경된 데이터를 전달하게 된다. 이러한 과정으로 백업을 할 수 있으며, Master 서버의 장애가 생겼을 경우 Slave 서버를 DB로 사용할 수 있다. 
![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/813b6171-4f3a-4147-9b65-43bba808756c)


DBMS의 부하 분산이다.

사용자의 폭주로 인해 1대의 DB서버로 감당할 수 없을 때, MySQL 레플리케이션을 이용하여 같은 DB 데이터를 여러대로 만들 수 있기 때문에 부하를 분산시켜줄 수 있다. 

위에서도 얘기했듯이 Master 서버는 등록/수정/삭제를 처리하는 서버로 사용하고, Slave 서버는 서버의 데이터를 읽는 용도로 사용하며 부하를 분산시킬 수 있다. 

![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/4a222976-2da0-414f-ad1a-fb96232ecbd9)



이 외에도 복제의 장점들엔 다음과 같은 것들이 있다. 


- 분석
  - 원본 데이터에 실시간 데이터가 생성되고, 원본 데이터에 성능 이슈없이 레플리카에서 분석을 할 수 있다.
- 원거리 데이터 분산
  - 원본데이터에 접근하지 않고도,  원격 사이트에서 사용 할 로컬 데이터 복사본을 생성할 수 있습니다.
 


## 복제의 원리
아래는 MySQL의 Master-Slave 복제 원리이다.
![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/f173acb8-e53a-4c2e-8082-3c153d455bc2)

MySQL에서 복제는 바이너리 로그 파일에 데이터에 대한 모든 변경사항을 기록한다.

1. 레플리카가 초기화가 된다면, 2개의 쓰레드 작업을 생성

2. 하나는 I/O 쓰레드로 원본 인스턴스에 연결하고 한 줄씩 바이너리 로그를 읽는다. 그리고 레플리카 서버의 Relay 로그에 해당 내용들을 복사.

3. 두번째 쓰레드는 SQL 쓰레드로, relay 로그를 읽고 레플리카 인스턴스에 최대한 빠르게 적용다.
<br><br><br><br>

## Replication 전 주의 사항
mysql replication을 진행하기 전 다음과 같이 주의해야 하는 몇 가지 사항들이 있다.

 

1. 호환성을 위해 Replication을 사용하는 MySQL의 버전은 동일하게 맞추기

2. Replication을 사용하기에 MySQL 버전이 다른 경우 Slave 서버가 상위 버전이어야 한다.

3. Replication을 가동시에 Master 서버, Slave 서버 순으로 가동시켜야 한다.

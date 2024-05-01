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


## Ubuntu 환경에서 구성
두 개의 우분투 환경에서 해보려다 간단하게 Docker를 사용해서 구성해보기로 했다.

### master DB 생성
master 컨테이너 실행 후 컨테이너 내부 접속, 설정 파일 수정을 위해 vim 설치

vim 설치가 안 될 경우, 로컬에서 my.cnf를 생성해 docker cp로 넣어주자. 이미지 마다 apt를 지원해주는 이미지도 있고 아닌 것도 있다. 

```
$ docker run -p 3306 --name mysql-master -e MYSQL_ROOT_PASSWORD=1234 -d mysql:8-debian

$ docker exec -it mysql-master /bin/bash

$ apt-get update
$ apt-get install -y vim
```

vi 명령어로 /etc/mysql/my.cnf 파일을 열고, 아래와 같이 2줄을 추가

```
log-bin=mysql-bin  
server-id=1
```

log bin
업데이트되는 모든 쿼리들이 Binary log 파일에 기록된다. 기본적으로 Binary log 파일은 MySQL의 data directory인 /var/lib/mysql/ 에 호스트명-bin.000001, 호스트명-bin.000002 형태로 생성된다.

 

이때, log-bin 설정을 변경하면 Binary log 파일의 경로와 파일명의 접두어를 변경할 수 있다.

위에선 log-bin=mysql이라 설정했기 때문에 mysql-bin.000001, mysql-bin.000002 이름으로로 Binary log 파일이 생성된다.

 

server-id
설정에서 서버를 식별하기 위한 고유 ID값이다. master, slave 각각 다르게 설정해야 한다.

 

 

도커를 재시작하여 설정 변경 적용 후 도커 내부에 다시 접속하여 설정이 제대로 적용되었는지 확인

```
$ docker restart mysql-master

$ docker exec -it mysql-master /bin/bash
$ mysql -u root -p 
mysql> SHOW MASTER STATUS\G
```

현재 바이너리 로그 파일명이고, Position은 현재 로그의 위치를 나타낸다.

![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/7d307af4-9a89-4712-9a5f-b5e84d2c98b5)

### master DB에 계정 생성

master DB에서 사용할 계정을 생성한다. 이 계정이 slave DB에서 복제할 예정이다. dgjinsu 라는 계정을 새로 생성하고, 모든 ip에 대해서 권한을 열어준다.

```
$ CREATE USER 'dgjinsu'@'%' IDENTIFIED BY '1234';

//sha256_password
$ ALTER USER 'dgjinsu'@'%' IDENTIFIED WITH mysql_native_password BY '1234';

$ GRANT REPLICATION SLAVE ON *.* TO 'dgjinsu'@'%';

$ FLUSH PRIVILEGES;
```

MySQL 5.8부터는 Password Auth방식이 caching_sha2_password 방식으로 변경되었다고 한다. 따라서 위와 같이 유저를 생성할 때 IDENTIFIED WITH mysql_native_password BY 로 생성해야한다. 그렇지 않으면 아래의 에러를 만날 수 있다.

```
error connecting to master 'replication
user@mysql-primary:3306' - retry-time: 60 retries: 1 message: Authentication plugin 'caching
sha2_password' reported error: Authentication requires secure connection.
```

전부 입력했다면 방금 생성된 계정이 보일 것이다.
```
$ SELECT User, Host FROM mysql.user;
```

![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/d1bb6f33-222a-4aa3-bb09-341eaa6aaabf)



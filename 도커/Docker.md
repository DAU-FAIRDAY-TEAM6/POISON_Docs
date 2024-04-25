## 도커란?
**도커(Docker)** 는 컨테이너 기반 가상화 플랫폼으로, 응용 프로그램과 그 종속성을 격리된 환경인 컨테이너로 패키징하여 실행하는 기술이다. 
이를 통해 응용 프로그램을 서로 다른 환경에서도 일관되게 실행할 수 있고, 개발 환경과 운영 환경 사이의 차이로 인한 문제를 줄일 수 있다. 
도커 컨테이너는 가볍고 빠르며 확장성이 좋아서 개발 및 배포 프로세스를 간소화하는 데 사용된다.

<br>

> 컨테이너 : 가상화 기술을 이용하여 어플리케이션과 개발 환경을 격리된 공간에서 실행하는 단위

<br>


**도커 컴포즈(Docker Compose)** 는 여러 개의 도커 컨테이너를 정의하고 실행하기 위한 도구로, 하나의 설정 파일로 여러 개의 컨테이너를 관리하고, 컨테이너 간의 네트워크 및 종속성을 설정하는 데 사용된다. 
주로 복잡한 응용 프로그램이 여러 컴포넌트로 구성되어 있을 때 사용한다.

<br>

> Virtual Machine vs Docker

![image](https://github.com/DAU-FAIRDAY-TEAM6/POISON_Docs/assets/97269799/3bd741be-ac95-488e-bed3-ef539d8cd713)

컨테이너 기술이 아닌 기존의 가상화 방식은 주로 OS를 가상화했다. 
VMware, VirtualBox와 같은 가상머신은 호스트 OS 위에 게스트 OS 전체를 가상화하여 사용하는 방식으로 도커의 컨테이너 방식과는 큰 차이가 있다.

- 가상 머신
  - 가상머신은 호스트 운영체제 위에 가상화된 하드웨어 계층을 생성하고, 각 가상 머신은 독립된 운영체제, 커널, 드라이버 등을 가짐
  - 이로 인해 무겁고 높은 자원 소비가 필요
  - 운영체제의 부팅 과정이 필요하므로 시간이 오래 걸림
  - 독립된 운영체제를 가지므로 메모리, 디스크 공간 등 자원을 많이 소비
<br>

- Docker 컨테이너
  - Docker 컨테이너는 호스트 운영체제의 커널을 공유하며, 가볍게 격리된 환경을 생성
  - 가상 머신보다 더 가벼우며 효율적으로 실행
  - 이미지와 컨테이너 레이어를 사용하여 빠르게 생성되며, 실행 속도가 매우 빠름
  - 컨테이너는 호스트 운영체제의 커널을 공유하므로 가볍고 효율적으로 자원을 활용

<br>
결론만 얘기하면 기존 가상머신은 무겁고 느리지만, 도커 컨테이너는 가볍고 빠르게 실행되며 호스트의 운영체제의 커널을 공유하는 방식으로 동작한다는 것이다. 또한 컨테이너 기술은 애플리케이션 배포와 관리를 더 효율적으로 처리할 수 있는 방법을 제공한다. 
<br><br>


## 도커의 사용 목적
### 환경 일치성
다양한 환경에서 동일한 실행 환경을 보장한다. 개발 환경과 운영 환경의 차이로 인한 문제를 방지하며, 응용 프로그램을 어디서든 실행할 수 있다.

### 편리한 배포
도커 컨테이너는 이미지로 패키징되어 배포되므로, 어플리케이션 배포가 간단해진다. 이미지를 공유하거나 배포할 때 용이하며, 빠른 확장이 가능하다.

### 격리된 환경
도커는 각 컨테이너를 격리된 환경으로 실행하므로, 하나의 컨테이너에서 발생한 문제가 다른 컨테이너에 영향을 주지 않는다.

### 자원 효율성
가상 머신과 비교해 더 가볍고 빠르며, 호스트 시스템의 리소스를 효율적으로 활용할 수 있다.

### 스케일링
컨테이너 기반 아키텍처는 쉬운 스케일링이 가능하여 요구에 따라 응용 프로그램을 확장할 수 있다.

<br>
국 도커란 개발을 편하기 하기 위한 도구이다. 개발자에게 개발 환경 세팅이란 번거럽고 시간이 많이 소요되는 작업이다. 특히 여러 개발자가 협업을 하는 경우, 각자 다른 운영체제나 라이브러리 버전으로 인해 일관된 개발 환경을 유지하기 어려울 수 있다. 하지만 도커를 사용하면 각각의 프로젝트를 격리된 컨테이너로 실행하여 개발할 수 있다. 이로써 각자의 개발 환경을 구성하는 번거로움을 덜 수 있고, 더욱 효율적인 개발과 협업이 가능해지는 것이다.
<br><br>


## 도커 사용 에시
**웹 개발** : 도커를 사용하여 웹 애플리케이션을 개발하면, 개발 환경을 동일하게 설정하고 다른 팀원과의 협업을 용이하게 할 수 있다. 개발 중인 애플리케이션의 서버, 데이터베이스, 캐싱 시스템 등을 각각의 도커 컨테이너로 실행하면 환경 일치성을 유지하면서 작업할 수 있다.


**서버 개발** : 마이크로서비스 아키텍처에서는 각 서비스를 독립적인 도커 컨테이너로 구성하여 개발하고 배포할 수 있다. 각 서비스는 독립된 코드베이스와 종속성을 가지며, 개별적으로 스케일링이 가능하다.


**AI 모델 개발** : AI 모델을 개발하고 배포할 때도 도커를 활용할 수 있다. 예를 들어, AI 모델을 실행하는 도커 컨테이너를 생성하고 배포할 수 있다. 이 컨테이너는 모델 추론을 수행하고, 필요한 라이브러리 및 종속성을 포함할 수 있다.


<br><br>


## 도커 이미지 && 도커 컨테이너
### 도커 이미지(Docker Image)
도커 이미지는 컨테이너를 만드는 데 사용되는 읽기 전용(Read-only) 템플릿이다.
컨테이너 실행에 필요한 파일과 설정값 등을 포함하고 있는 도커파일을 만든 후 Dockerfile을 빌드 하여 이미지를 만든다.

<br>

### 도커 컨테이너(Docker Container)
도커 이미지를 실행한 상태
이미지로 컨테이너를 생성하면 이미지의 목적에 맞는 파일이 들어있는 파일 시스템과
격리된 시스템 자원 및 네트워크를 사용할 수 있는 독립된 공간이 생성된다.
이것을 도커 컨테이너라고 한다.
도커 컨테이너는 읽기 전용인 이미지에 변경된 사항을 저장하는 컨테이너 계층(Layer)에 저장한다.

![image](https://github.com/dgjinsu/POISON_Docs/assets/97269799/4690a59f-4b5c-4623-86f1-f31c47bfc6c9)
도커 이미지를 도넛 레시피에 비유한다면, 도커 컨테이너는 해당 레시피를 이용해 만든 도넛으로 비유할 수 있다.
**하나의 도넛 레시피에서 여러 가지 맛의 도넛을 만들 수 있는 것과 같이, 하나의 도커 이미지로 여러 개의 도커 컨테이너를 만들 수 있다.**
또한, 기존의 도넛 레시피를 수정하게 되어도, 이미 기존 레시피로 만들어진 도넛에는 영향이 없듯이, 이처럼 도커 이미지를 변경해도 이미 실행 중인 도커 컨테이너에는 영향을 주지 않는다.

<br>

### 기본적인 도커 명령어
```
docker [대상] [액션]

→ [대상] : container(생략 가능), image, volume, network 등

→ [액션] : ls, inspect, start, run 등
```

![image](https://github.com/dgjinsu/POISON_Docs/assets/97269799/7460a4d5-8d70-4edf-b058-f4b569e49678)
<br>

- docker (container) create
  - 컨테이너를 생성하고 자동으로 시작하지는 않음
 
```
root@DH:~# docker create --name testos centos
Unable to find image 'centos:latest' locally
latest: Pulling from library/centos
a1d0c7532777: Pull complete
Digest: sha256:a27fd8080b517143cbbbab9dfb7c8571c40d67d534bbdee55bd6c473f432b177
Status: Downloaded newer image for centos:latest
875366cc4662d6ccdc21dfbaa654ed3eee74bb54d6a2ce34333a62924f7e0272
```

centos 이미지를 사용해서 컨테이너를 생성해 주는 명령어이다.
--name 옵션을 추가하여 컨테이너명은 testos로 설정
→ name 옵션을 쓰지 않으면 임의의 name이 부여된다.

이미 생성된 컨테이너의 컨테이너 명을 바꾸고 싶으면 docker rename [현재 이름] [바꿀 이름] 명령어를 사용한다.
컨테이너 명을 변경하여도 컨테이너 ID는 변경되지 않는다.

로컬 리포지토리에 이미지가 없으면 기본으로 docker hub에서 이미지를 pull 한다.
한번 pull 한 이미지는 재사용이 가능하다.

컨테이너를 생성할 때 옵션을 써줄 수도 있다.

```
docker create -it --name testos2 centos
```
![image](https://github.com/dgjinsu/POISON_Docs/assets/97269799/248a9788-62a2-4812-97f5-43ab2a081f7f)

<br><br><br>

- docker ps
  - 실행(Up) 중인 컨테이너들의 목록을 확인
  - docker container ls와 같음
  - -a (all) 옵션을 함께 써주면 실행 중이지 않은 컨테이너를 포함하여 전체 컨테이너 목록을 출력합니다.

```
root@DH:~# docker ps
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS          PORTS     NAMES
adb6732a399d   centos    "/bin/bash"   51 seconds ago   Up 50 seconds             testos2
```


```
root@DH:~# docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS          PORTS     NAMES
adb6732a399d   centos    "/bin/bash"   55 seconds ago   Up 54 seconds             testos2
875366cc4662   centos    "/bin/bash"   5 hours ago      Created                   testos
```
<br><br><br>

- docker start
  - 컨테이너를 시작(실행)
  - 생성해둔 컨테이너를 시작할 수 있음

 ```
root@DH:~# docker start -ai testos
[root@151f3b70b5a4 /]#
```

컨테이너(testos)를 시작하면서 -ai 옵션을 사용해 해당 컨테이너 내부로 접근하여 표준 입력을 받을 수 있도록 할 수 있다.

해당 컨테이너에 접근한 상태로 exit 명령을 사용하면, /bin/bash가 종료되면서 컨테이너도 함께 종료된다.
때문에 순차적으로 **Ctrl + P, Ctrl + Q** 를 눌러 컨테이너 실행 상태를 유지한 채로 빠져나온 후, 컨테이너가 실행 중(Up)인지 확인할 수 있다.
<br><br><br>



- docker stop
  - 실행 중인 컨테이너를 종료

```
root@DH:~# docker stop testos
testos
```
<br><br><br>

- docker run
  - 컨테이너를 시작하고 COMMAND를 실행
  - 로컬에 이미지가 있다면 해당 이미지로 실행하고, 없으면 도커허브에서 다운로드 후 실행
  - create + start

```
root@DH:~# docker run -dit --name test centos
5d56fc765e3780fb06f5f3d5a66935e1a087087d7b9ab69e979e830773603a81

root@DH:~# docker ps
CONTAINER ID   IMAGE     COMMAND       CREATED        STATUS        PORTS     NAMES
5d56fc765e37   centos    "/bin/bash"   1 second ago   Up 1 second             test
```
<br><br><br>

-d 옵션을 사용해 사용자가 직접 컨테이너 안으로 접근하지 않고, 컨테이너의 COMMAND를 백그라운드로 실행할 수 있다.
컨테이너를 시작할 때, 명령어의 맨 뒤에 임의로 COMMAND를 정의할 수 있다.
COMMAND(/bin/date)가 종료되면서 컨테이너도 함께 종료된 것을 확인할 수 있다.
```
root@DH:~# docker run -it --name date centos /bin/date
Tue Jun 28 08:56:41 UTC 2022

root@DH:~# docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED              STATUS                          PORTS     NAMES
24a654120847   centos    "/bin/date"   About a minute ago   Exited (0) About a minute ago             date
```
<br><br><br>

- docker logs
  - 컨테이너의 PID=1 프로세스의 STDIN/STDOUT/STDERR를 출력 가능
```
root@DH:~# docker logs -f pingtest
PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.019 ms
64 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.036 ms
64 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.069 ms
```
<br><br><br>


- docker cp
  - 컨테이너와 호스트 간의 파일 복사'

 ```
root@DH:~# touch example.txt
root@DH:~# ls
example.txt

root@DH:~# docker run -dit --name test centos
5e43e97c988e78202f4d6dcb2b68b153c0a3c91e80ac2bdb5b8b7ae2a39f0592

root@DH:~# docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED         STATUS         PORTS     NAMES
5e43e97c988e   centos    "/bin/bash"   6 seconds ago   Up 5 seconds             test

root@DH:~# docker cp ~/example.txt test:/

root@DH:~# docker exec test /bin/ls example.txt
example.txt

root@DH:~# docker cp test:/example.txt ~/example2.txt

root@DH:~# ls
example.txt  example2.txt
```


<<br><<br><<br><<br>

## 도커로 MySQL 띄우기
```
$ docker pull mysql
```

<br>

```
$ docker pull mysql
Using default tag: latest
latest: Pulling from library/mysql
4be315f6562f: Pull complete
96e2eb237a1b: Pull complete
8aa3ac85066b: Pull complete
ac7e524f6c89: Pull complete
f6a88631064f: Pull complete
15bb3ec3ff50: Pull complete
ae65dc337dcb: Pull complete
573c3c7fa18d: Pull complete
9d10771b98b8: Pull complete
3d8ef442614b: Pull complete
7dc17a6cea26: Pull complete
752752efdaea: Pull complete
Digest: sha256:2dafe3f044f140ec6c07716d34f0b317b98f8e251435abd347951699f7aa3904
Status: Downloaded newer image for mysql:latest
```

<br>
다운로드한 도커 이미지를 확인해보자, 내 경우에는 도커 Desktop을 활용해서 설치 유무를 확인했는데, 이 경우가 아니라면 명령어로도 확인할 수 있다.

- 아래는 도커 데스크탑을 활용하여 내가 설치한 Docker image 항목들이다.
![image](https://github.com/dgjinsu/POISON_Docs/assets/97269799/0f0305b9-0dd1-45f5-9f6d-b3b91c4a70f1)


- 명령어를 통한 Docker image 확인은 아래와 같다.
```
$ docker images
REPOSITORY      TAG       IMAGE ID       CREATED      SIZE
mysql           latest    96d0eae5ed60   9 days ago   524MB
```

이제 생성한 Mysql 이미지를 Container에 올려보도록하자.

```
$ docker run -it -e MYSQL_ROOT_PASSWORD=1234 -d -p 3308:3306 -v 내 로컬에 있는 폴더 경로:도커 폴더 경로 mysql
```

위에 작성한 명령어를 뜯어 보면 다음과 같다. 
<br>

run : 도커 이미지를 컨테이너로 생성하면서 실행을 동시에 해준다.

-i : 컨테이너를 실행할 때 컨테이너 쪽 표준 입력과의 연결을 그대로 유지한다. 그러므로 컨테이너 쪽 셀에 들어가서 명령어를 실행할 수 있다.

-t : 유사터미널 기능을 활성화하는 옵션이다. 여기서 i 옵션을 사용하지 않으면 유사 터미널을 실행해도 입력할 수가 없으므로 통상적으로 -it를 합쳐서 사용한다.

-d : deamon 옵션으로서 도커가 백그라운드에서 계속 실행되게 한다.

-p : 포트 옵션으로서 <로컬에서 접속하는 포트>:<도커쪽에서 열리는 포트> 즉 내쪽에서 3308 포트로 접속하면, 도커쪽에서 3306으로 들어가게 된다. 나는 로컬 DB가 3306포트를 사용중이라서 3308포트를 사용하여 접속했다.

-v : 마운트 옵션으로서 내 로컬에 있는 폴더와 도커에 있는 폴더를 마운트 시켜준다. (마운트 옵션은 도커에 있는 데이터가 삭제되지 않고 꾸준히 관리되기를 원할때 걸어주는 옵션이므로 지속적으로 관리가 필요없는 경우는 없어도 무관하다)


만약 -v 옵션 즉, 마운트 옵션을 제외하고 만들고 싶다면 아래와 같이 입력하면 된다.


```
$ docker run -it -e MYSQL_ROOT_PASSWORD=1234 -d -p 3308:3306 mysql
```

성공적으로 DB에 잘 연결되는 걸 확인할 수 있다. 
![image](https://github.com/dgjinsu/POISON_Docs/assets/97269799/314faeee-ca4c-4a42-a959-35a5c78b79fb)


<br><br><br><br>

## Spring boot 컨테이너 생성 DB 연결
> 아래 내용은 같은 network 에 mysql 컨테이너가 띄워져있다 가정하고 작성하였습니다. 

### application.yml 작성
```
server:
  port: 8088
spring:

  profiles:
    active: test

  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://[컨테이너 이름]:3306/helloDev
```
- 기존의 localhost 대신 위에서 생성한 mysql-container의 이름을 넣어주어야 한다. 
- 이름 대신에 mysql-container의 IP 주소를 입력해도 되지만 Docker의 DNS가 동적으로 매핑해주니 이름으로 사용


### Docker file 작성
```
FROM openjdk:11-jre-slim

WORKDIR /app

# 빌드된 Spring Boot JAR 파일을 복사
COPY build/libs/demo-0.0.1-SNAPSHOT.jar [jar이름].jar

# JAR 파일 실행
CMD ["java", "-jar", "[jar이름].jar"]
```

<br><br><br>

### spring boot 이미지 생성 후 실행

1. jar 파일 생성
2. docker build -t hellodev-image . 해당 명령어를 입력하여 이미지 생성
3. 위와 동일하게 생성한 네트워크를 옵션으로 주어 이미지 실행.
  - docker run -d --name hellodev-container --network docker-network -p 8088:8088  hellodev-image
4. docker network inspect docker-network 명렁어를 통해 spring boot, mysql 컨테이너가 생성한 네트워크에 속하는지 확인.

![image](https://github.com/dgjinsu/POISON_Docs/assets/97269799/c933ded7-f0af-408c-92c6-84a979017069)


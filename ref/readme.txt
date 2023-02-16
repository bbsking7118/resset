1. pip install django
2. python.exe -m pip install --upgrade pip
3. django-admin startproject config .

4. python manage.py startapp shop => app 추가


5. models.py 작업 : 모델 매이킹
   templates 폴더 생성

6. aws mysql 생성 : admin xxxx5
7. db 연결작업
    1. pip install pymysql
    2. setting.py 수정
8. pip install pillow, python manage.py makemigrations, migrate, createsuperuser

9. views.py 수정, app.urls.py 와 config.urls.py admin.py 수정 => runserver
10. html 작성

11. aws s3 연결
    1. s3 버킷 만들고, 유저그룹및 유저 생성
    2. setting.py 추가
    3. pip install django-storages, boto3
    4. python manage.py collectstatic
    5. media storage : s3media.py 작성

12. restframework
    1. pip install djangorestframework, app 등록
    2. pip install django-rest-swagger==2.1.2, 기타 setting.py 추가
    => python manage.py collectstatic 한번더 실행
       잘못된 설치 pip install -U drf-yasg

    3. 인증
////////////////////////////////////////////////////////////////////////////////
// next
aws ec2 서버에 배포
1. ec2 instance 만들기
2. winscp로 연결... (키페어...)
3. sudo apt-get update, sudo apt-get install nginx, systemctl status nginx
4. 전용그룹과 계정 만들기
    sudo groupadd djangogroup, sudo useradd -g djangogroup -b /home -m -s /bin/bash django
    sudo mkdir -p /var/www/e2db
    sudo chown django:djangogroup /var/www/e2db
    sudo usermod -a -G djangogroup ubuntu
    sudo chmod g+w /var/www/e2db
5. 필요한 패키지 설치
    sudo apt-get install build-essential libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info libssl-dev
    sudo apt-get install python3-dev python3-pip python3-cffi python3-venv
    pip freeze > requirements.txt

    config/setting.py : DEBUG = False ALLOWED_HOST = ['.compute.amazonaws.com']


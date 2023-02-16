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
    sudo mkdir -p /var/www
    sudo chown django:djangogroup /var/www
    sudo usermod -a -G djangogroup ubuntu
    sudo chmod g+w /var/www
5. 필요한 패키지 설치
    python3 --version
    {
        sudo apt-get install python3.8
        sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
        sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2
        sudo update-alternatives --config python3 ==> 2선택
        python --version => python3.8.0

    }
    sudo apt-get install build-essential libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info libssl-dev
    sudo apt-get install python3-dev python3-pip python3-cffi python3-venv
    sudo apt-get install python3.8-venv
    파일질라 설치하고 연결

7. 소스업로드
    config/setting.py : DEBUG = False ALLOWED_HOST = ['.compute.amazonaws.com','127.0.0.1,'localhost']
    pip freeze > requirements.txt

    git push~

    (www 디렉토리에서)
    sudo git clone https://github.com/bbsking7118/e2db.git

    (cd /var/www/e2db)
    sudo python3.8 -m venv venv

6. 파이썬 가상환경 실행
    sudo -s
    source venv/bin/activate

    pip install -r requirements.txt
    pip install uwsgi

7. uwsgi 환경설정
    sudo mkdir run logs ssl
    sudo chown django:www-data run // sudo chown django-www-data logs
    vim /var/www/e2db/run/uwsgi.ini
[uwsgi]
uid = django
base = /var/www/e2db
home = %(base)/venv
chdir = %(base)
module = config.wsgi:application
env = DJANGO_SETTIONGS_MODULE=config.settings
master = true
processes = 5
socket = %(base)/run/uwsgi.sock
logto = %(base)/logs/uwsgi.log
chown-socket = %(uid):www-data
chmod-socket = 660
vacuum = true

    vim /etc/systemd/system/uwsgi.service
[Unit]
Description=uWSGI Emperor service

[Service]
ExecStart=/var/www/e2db/venv/bin/uwsgi --emperor /var/www/e2db/run
User=django
Group=www-data
Restart=on-failure
KillSignal=SIGQUIT
Type=notivy
NotifyAccess=all
StandardError=syslog

[Install]
WantedBy=munti-user.target

    systemctl start uwsgi // systemctl enable uwsgi // systemctl status uwsgi

8. nginx 설정
    cp etc/nginx/sites-available/default /etc/nginx/sites-available/e2db
    ln -s /etc/nginx/sites-available/onlineshop /etc/nginx/sites-enabled/
    vim /etc/nginx/nginx.conf
server_name_hash-bucket_size 128; => 여러개 있음. 앞에 #을 삭제해야함
    vim /etc/nginx/sites-available/e2db
upstream django {
    server unix:/var/www/e2db/run/uwsgi.sock;
}
server {
    listen 80:
    server_name [EC2 퍼블릭 DNS];
    charset utf-8;

    locatiton / {
        include     /etc/nginx/uwsgi_params;
        uwsgi_pass  django;
    }
}

    uginx -t // systemctl restart nginx





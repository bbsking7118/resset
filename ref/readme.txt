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
////////////////////////////////////////////////////////////////////////////////
// next
-. restframework
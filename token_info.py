DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # mysql 엔진 설정
        'NAME': 'django_db', # 데이터베이스 이름
        'USER': 'wooney', # 데이터베이스 연결시 사용할 유저 이름(개발자 계정)
        'PASSWORD': '12345', # 유저 패스워드		
        'HOST': 'localhost', 
        'PORT': '3306'
    }
}
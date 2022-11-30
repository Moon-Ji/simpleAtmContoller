## 서버 실행

#### DB 설정
```
CREATE DATABASE Atm
    DEFAULT CHARACTER SET = 'utf8mb4';
```

/server 에서 
```
flask db init
flask db migrate
flask db upgrade
```

#### secret.py 생성 
```
username = ''
db_pw = ''
secret_key = ''
jwt_secret_key = ''
```

#### 서버 실행
```
pip install -r requirements.txt
flask run
```
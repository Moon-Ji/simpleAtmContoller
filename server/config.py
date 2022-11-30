from secret import username, db_pw, secret_key, jwt_secret_key

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+username+':'+db_pw+'@localhost:3306/atm?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SESSION_TYPE = 'filesystem'
SECRET_KEY = secret_key
from db_connect import db
from flask_restx import fields

class Account(db.Model):
    __tablename__ = "Account"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50))
    card_number = db.Column(db.String(20), nullable=False)
    account_number = db.Column(db.String(20), nullable=False)
    pin = db.Column(db.Integer, nullable=False)
    balance =db.Column(db.Integer)
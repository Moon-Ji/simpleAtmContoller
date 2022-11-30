from db_connect import db
from flask_restx import fields

class Record(db.Model):
    __tablename__ = "Record"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    account_number = db.Column(db.String(20), nullable=False)
    deposit = db.Column(db.Integer)
    withdraw = db.Column(db.Integer)
    midified_at = db.Column(db.String(50))
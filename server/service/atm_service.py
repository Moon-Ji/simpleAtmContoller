from flask import abort

from db_connect import db
from models.account import Account
from models.record import Record

from datetime import datetime

def insert_card(request_body):
    print(request_body)
    card_number = request_body["card_number"]
    pin = request_body["pin"]

    account = Account.query.filter(Account.card_number == card_number).first()
    if not account:
        abort(400, "Account Not Found")
    
    pin_check = account.pin
    if pin != pin_check:
        abort(400, "Wrong pin number")
    
    return account.account_number

def check_balance(request_body):
    account_number = request_body["account_number"]
    account = Account.query.filter(Account.account_number == account_number).first()
    if not account:
        abort(400, "Account Not Found")

    return account.balance

def deposit_service(request_body):
    account_number = request_body["account_number"]
    deposit = request_body["deposit"]

    account = Account.query.filter(Account.account_number == account_number).first()
    try:
        account.balance += deposit

        new_record = Record(
            account_number=account_number,
            deposit=deposit,
            midified_at=datetime.now()
        )

        db.session.add(new_record)
        db.session.commit()
    except:
        return False
    else:
        return True

def withdraw_service(request_body):
    account_number = request_body["account_number"]
    withdraw = request_body["withdraw"]

    account = Account.query.filter(Account.account_number == account_number).first()
    try:
        if account.balance < withdraw:
            return abort(400, "balance is insufficient")

        account.balance -= withdraw

        new_record = Record(
            account_number=account_number,
            withdraw=withdraw,
            midified_at=datetime.now()
        )

        db.session.add(new_record)
        db.session.commit()
    except:
        return False
    else:
        return True


from flask import request
from flask_restx import Resource, Namespace, fields

from service.atm_service import insert_card, check_balance, deposit_service, withdraw_service

atm = Namespace(name="Atm", description="Atm service")

@atm.route('/insert')
class Insert(Resource):
    @atm.response(200, "success")
    @atm.response(400, "falied")
    def get(self):
        """insert card"""
        request_body = request.get_json()
        return insert_card(request_body), 200

@atm.route('/balance')
class Insert(Resource):
    @atm.response(200, "success")
    @atm.response(400, "falied")
    def get(self):
        """check balance"""
        request_body = request.get_json()
        return check_balance(request_body), 200

@atm.route("/deposit")
class Deposit(Resource):
    @atm.response(200, "success")
    @atm.response(400, "falied")
    def post(self):
        """deposit"""
        request_body = request.get_json()
        return deposit_service(request_body), 200

@atm.route("/withdraw")
class Withdraw(Resource):
    @atm.response(200, "success")
    @atm.response(400, "falied")
    def post(self):
        """withdraw"""
        request_body = request.get_json()
        return withdraw_service(request_body), 200

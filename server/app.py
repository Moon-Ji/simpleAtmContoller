from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api

from controller.atm_controller import atm

from db_connect import db
import config

def create_app():
    app = Flask(__name__)
    api = Api(app, title="ATM service")
    api.add_namespace(atm, "/atm")
    
    app.config.from_object(config)
    db.init_app(app)
    Migrate(app, db)

    return app

if __name__ == "__main__":
    create_app().run(debug=True)
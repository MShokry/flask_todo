from flask import Flask, Blueprint
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
ma = Marshmallow(app)

# from src import models
from src.task import Task
from src.user import Users
from src.Auth import Login

#api = Api(app)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)
app.register_blueprint(api_bp, url_prefix='/api')

# Route
api.add_resource(Task, '/Task')
api.add_resource(Users, '/Users')
api.add_resource(Login, '/Login')


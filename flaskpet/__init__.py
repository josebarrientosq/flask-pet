from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pet.db'
db = SQLAlchemy(app)

import flaskpet.routes
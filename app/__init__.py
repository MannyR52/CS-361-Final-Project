from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
# export FLASK_APP=app
# flask shell
# from app import db
# db.create_all()
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from app.users.routes import users
from app.workouts.routes import workouts
from app.main.routes import main
from app.calculator.routes import calculator
from app.random.routes import gen_random

app.register_blueprint(users)
app.register_blueprint(workouts)
app.register_blueprint(main)
app.register_blueprint(calculator)
app.register_blueprint(gen_random)


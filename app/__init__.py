from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_login import LoginManager
from threading import Thread
from app import jobs_scheduler

# app
def create_app():
    app = Flask(__name__)
    config = app.config.from_object(Config)
    Thread(target=jobs_scheduler.main).start()
    return app


app = create_app()

# admin
admin = Admin(app)

# db
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# login
login = LoginManager(app)
login.login_view = 'login'


from app import routes, models

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from rq import Queue

from settings import settings
from worker import conn


app = Flask(__name__)
app.config['SECRET_KEY'] = settings['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = settings['DB_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

q = Queue(connection=conn)

from project.tasks import tasks

app.register_blueprint(tasks)


from project.models import Url

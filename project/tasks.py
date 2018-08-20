from flask import Blueprint, render_template, request
import requests
from project import db
from project.models import Url

tasks = Blueprint('tasks', __name__, template_folder='templates')


@tasks.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['input_url']
        resp = requests.get(url)
        words = len(resp.text.split())
        new_record = Url()
        new_record.url = url
        new_record.words = words
        db.session.add(new_record)
        db.session.commit()
    urls = Url.query.distinct(Url.url).all()
    print(urls, type(urls))
    return render_template('index.html', urls=urls)

from flask import Blueprint, render_template, request
import requests
from project import db, q
from project.models import Url

tasks = Blueprint('tasks', __name__, template_folder='templates')


@tasks.route('/', methods=['GET', 'POST'])
def home():
    urls = Url.query.distinct(Url.url).all()
    if request.method == 'POST' and request.form['input_url']:
        url = request.form['input_url']
        job = q.enqueue_call(func=count_words_at_url, args=(url,))
        return render_template('index.html', urls=urls, job_id=job.id)
    return render_template('index.html', urls=urls)


def count_words_at_url(url):
    resp = requests.get(url)
    words = len(resp.text.split())
    new_record = Url(url=url, words=words)
    db.session.add(new_record)
    db.session.commit()

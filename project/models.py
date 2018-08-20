from project import db


class Url(db.Model):
    _tablename_ = 'urls'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(500))
    words = db.Column(db.Integer, default=0)

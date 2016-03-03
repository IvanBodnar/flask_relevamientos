from relevamientos.app import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    fullname = db.Column(db.String(80))
    level = db.Column(db.Integer)

    def __init__(self, username, password, fullname, level=20):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.level = level

    def __repr__(self):
        return '<User> %s' % self.username
from relevamientos.app import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    fullname = db.Column(db.String(80))
    is_boss = db.Column(db.Boolean)

    def __init__(self, username, password, fullname, is_boss=False):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.is_boss = is_boss

    def __repr__(self):
        return '<User> %s' % self.username
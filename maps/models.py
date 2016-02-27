from relevamientos.app import db


class Calles(db.Model):
    __tablename__ = 'calles'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150))

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
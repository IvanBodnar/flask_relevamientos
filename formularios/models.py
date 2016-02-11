from relevamientos.app import db
import datetime


class Formulario1(db.Model):
    __tablename__ = 'formulario1'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, default=datetime.datetime.now())
    vehiculo1 = db.Column(db.String(20))
    vehiculo2 = db.Column(db.String(20))
    causa = db.Column(db.String(20))
    heridos = db.Column(db.Integer)
    observaciones = db.Column(db.String(200))

    def __init__(self, vehiculo1, vehiculo2, causa, heridos, observaciones):
        self.vehiculo1 = vehiculo1
        self.vehiculo2 = vehiculo2
        self.causa = causa
        self.heridos = heridos
        self.observaciones = observaciones
import datetime
import pytz
from relevamientos.app import db


class Formulario1(db.Model):

    __tablename__ = 'formulario1'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=True)
    hora_dato = db.Column(db.Time, nullable=True)
    hora_hecho = db.Column(db.Time, nullable=True)
    vehiculo1 = db.Column(db.String(20))
    vehiculo2 = db.Column(db.String(20))
    vehiculo3 = db.Column(db.String(20))
    vehiculo4 = db.Column(db.String(20))
    causa = db.Column(db.String(20))
    heridos = db.Column(db.Integer)
    obitos = db.Column(db.Integer)
    observaciones = db.Column(db.String(2000))
    calle1 = db.Column(db.String(150))
    calle2 = db.Column(db.String(150))
    altura = db.Column(db.Integer)
    lat = db.Column(db.Float)
    long = db.Column(db.Float)
    precision = db.Column(db.Float)

    def __init__(self, hora_hecho, vehiculo1, vehiculo2, vehiculo3, vehiculo4, causa, heridos, obitos, observaciones,
                 calle1, calle2, altura, lat=None, long=None, precision=None):

        self.ar = pytz.timezone('America/Buenos_Aires')
        self.cur_time = pytz.utc.localize(datetime.datetime.utcnow()).astimezone(self.ar)
        self.tz_curtime = self.cur_time.strftime('%H:%M')

        self.fecha = self.ar.localize(datetime.datetime.now())
        self.hora_dato = self.tz_curtime
        self.hora_hecho = hora_hecho
        self.vehiculo1 = vehiculo1
        self.vehiculo2 = vehiculo2
        self.vehiculo3 = vehiculo3
        self.vehiculo4 = vehiculo4
        self.causa = causa
        self.heridos = heridos
        self.obitos = obitos
        self.observaciones = observaciones
        self.calle1 = calle1
        self.calle2 = calle2
        self.altura = altura
        self.lat = lat
        self.long = long
        self.precision=precision



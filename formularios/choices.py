from relevamientos.app import db
from maps.models import Calles

VEHICULOS = [('ap', 'AP'),
             ('tp', 'TP'),
             ('moto', 'Moto'),
             ('peaton', 'Peatón')]

CAUSA = [('lesiones', 'Lesiones'),
         ('homicidio', 'Homicidio')]

HERIDOS = [(x, str(x)) for x in range(1, 11)]

query_calles = Calles.query.order_by(Calles.nombre).all()

CALLES = [x.nombre for x in query_calles]

#print(CALLES)


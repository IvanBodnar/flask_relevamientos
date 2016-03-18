from relevamientos.app import db
from maps.models import Calles

VEHICULOS = [('', ''),
             ('ap', 'AP'),
             ('tp', 'TP'),
             ('moto', 'Moto'),
             ('bicicleta', 'Bicicleta'),
             ('peaton', 'Peatón'),
             ('camion', 'Camión'),
             ('camioneta', 'Camioneta'),
             ('taxi', 'Taxi'),
             ('micro', 'Micro'),
             ('transporte escolar', 'Transporte Escolar'),
             ('ambulancia', 'Ambulancia'),
             ('fuerzas seguridad', 'Fuerzas de Seguridad'),
             ('tren', 'Tren')]

CAUSA = [('lesiones', 'Lesiones'),
         ('homicidio', 'Homicidio')]

HERIDOS = [(x, str(x)) for x in range(0, 11)]

OBITOS = [(x, str(x)) for x in range(0, 6)]

query_calles = Calles.query.order_by(Calles.nombre).all()

CALLES = [x.nombre for x in query_calles]

#print(CALLES)


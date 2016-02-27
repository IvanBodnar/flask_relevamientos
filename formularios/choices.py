from relevamientos.app import db
from maps.models import Calles

VEHICULOS = [('ap', 'AP'),
             ('tp', 'TP'),
             ('moto', 'Moto'),
             ('peaton', 'Peatón')]

CAUSA = [('lesiones', 'Lesiones'),
         ('homicidio', 'Homicidio')]

HERIDOS = [(x, str(x)) for x in range(1, 11)]

#CALLES = [x for x in Calles.query.all()]


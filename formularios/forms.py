from flask_wtf import Form
from wtforms import validators, SelectField, TextAreaField, StringField
from formularios.choices import *

# Choices come from formularios.choices.py
class Formulario1Form(Form):
    calle1 = StringField('Calle1')
    vehiculo1 = SelectField('Vehículo 1', choices=VEHICULOS)
    vehiculo2 = SelectField('Vehículo 2', choices=VEHICULOS)
    causa = SelectField('Causa', [validators.DataRequired(message='Campo requerido')], choices=CAUSA)
    heridos = SelectField('Heridos', choices=HERIDOS, coerce=int)
    observaciones = TextAreaField('Observaciones')
    lat = StringField('Lat', default='0.0')
    long = StringField('Long', default='0.0')
    accuracy = StringField('Precision', default='0.0')
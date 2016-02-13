from flask_wtf import Form
from wtforms import validators, StringField, SelectField, TextAreaField
from formularios.choices import *

# Choices come from formularios.choices.py
class Formulario1Form(Form):
    vehiculo1 = SelectField('Vehículo 1', choices=VEHICULOS)
    vehiculo2 = SelectField('Vehículo 2', choices=VEHICULOS)
    causa = SelectField('Causa', [validators.DataRequired(message='Campo requerido')], choices=CAUSA)
    heridos = SelectField('Heridos', choices=HERIDOS, coerce=int)
    observaciones = TextAreaField('Observaciones')
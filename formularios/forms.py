from flask_wtf import Form
from wtforms import validators, SelectField, TextAreaField, StringField, IntegerField
from formularios.choices import *


def validate_int(form, field):
    try:
        int(field.data)
    except:
        raise validators.ValidationError('Ingrese un Número')

# Validates if a lone number was entered in a street field
def validate_street_words(form, field):
    if field.data.isdigit():
        raise validators.ValidationError('Ingrese Nombre de Calle Válido')


# Choices come from formularios.choices.py
class Formulario1Form(Form):

    hora_hecho = SelectField('Hora del Hecho', choices=HORA)
    vehiculo1 = SelectField('Vehículo 1', choices=VEHICULOS)
    vehiculo2 = SelectField('Vehículo 2', choices=VEHICULOS)
    vehiculo3 = SelectField('Vehículo 3', choices=VEHICULOS)
    vehiculo4 = SelectField('Vehículo 4', choices=VEHICULOS)
    causa = SelectField('Causa', [validators.DataRequired(message='Campo Requerido')], choices=CAUSA)
    heridos = SelectField('Cantidad de Heridos', choices=HERIDOS, coerce=int)
    obitos = SelectField('Cantidad de Obitos', choices=OBITOS, coerce=int)
    observaciones = TextAreaField('Observaciones')
    calle1 = StringField('Calle 1', [validate_street_words])
    calle2 = StringField('Calle 2', [validate_street_words])
    altura = IntegerField('Altura (sólo si no es intersección)', [validators.optional(), validate_int])
    lat = StringField('Latitud', default='0.0')
    long = StringField('Longitud', default='0.0')
    precision = StringField('Precision', default='0.0')


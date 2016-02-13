from flask_wtf import Form
from wtforms import validators, StringField, PasswordField


class LoginForm(Form):
    username = StringField('Usuario', [validators.DataRequired(message='Campo requerido')])
    password = PasswordField('Contraseña', [validators.DataRequired(message='Campo requerido')])
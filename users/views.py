from relevamientos.app import app
from flask import render_template
from users.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('users/index.html')


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    return render_template('users/login.html', form=form)
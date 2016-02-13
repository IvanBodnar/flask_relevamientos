from relevamientos.app import app
from flask import render_template, redirect, request, url_for, session
from users.forms import LoginForm
from users.models import Users


@app.route('/')
@app.route('/index')
def index():
    return render_template('users/index.html')


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    error = None

    # Manage the 'next'
    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)

    # Check if user and pass are correct
    if form.validate_on_submit():
        user = Users.query.filter_by(
            username=form.username.data,
            password=form.password.data
        ).first()
        if user:
            session['username'] = form.username.data
            if 'next' in session:
                next = session.get('next')
                session.pop('next')
                return redirect(next)
            else:
                return redirect(url_for('formularios')) # TODO hacer funcion y html para formularios

    return render_template('users/login.html', form=form, error=error)




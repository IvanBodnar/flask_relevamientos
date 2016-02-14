from relevamientos.app import app
from flask import render_template, redirect, request, url_for, session, flash
from users.forms import LoginForm
from users.models import Users
from decorators import login_required


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
            # Agregar usuario e is_boss a la sesion
            session['username'] = form.username.data
            session['is_boss'] = user.is_boss

            # Probar
            flash('Usuario %s logueado' % (user.fullname))

            if 'next' in session:
                next = session.get('next')
                session.pop('next')
                return redirect(next)
            else:
                return redirect(url_for('formularios'))
        else:
            error = 'Usuario o contraseña incorrectos'

    return render_template('users/login.html', form=form, error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('username')
    session.pop('is_boss')
    return redirect(url_for('index'))





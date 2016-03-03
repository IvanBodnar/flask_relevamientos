from relevamientos.app import app
from flask import render_template, redirect, request, url_for, session, flash
from users.forms import LoginForm
from users.models import Users
from decorators import login_required, directivo_required, admin_required


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
        username = form.username.data.lower()
        password = form.password.data.lower()
        user = Users.query.filter_by(
            username=username,
            password=password
        ).first()
        if user:
            # Add user end level to session
            session['username'] = username
            session['level'] = user.level

            # Test
            flash('Usuario %s logueado' % (user.fullname.title()))

            '''
            if 'next' in session:
                next = session.get('next')
                session.pop('next')
                return redirect(next)
            else:
            '''
            # Check access level
            if session['level'] == 20:
                return redirect(url_for('formularios'))
            elif session['level'] == 10:
                return redirect(url_for('directivos'))
            elif session['level'] == 0:
                return redirect(url_for('admin'))

        else:
            error = 'Usuario o contraseña incorrectos'

    return render_template('users/login.html', form=form, error=error)


@app.route('/admin')
@login_required
@admin_required
def admin():
    return render_template('users/admin.html')


@app.route('/directivos')
@login_required
@directivo_required
def directivos():
    return render_template('users/directivos.html')


@app.route('/logout')
@login_required
def logout():
    session.pop('username')
    session.pop('level')
    return redirect(url_for('index'))





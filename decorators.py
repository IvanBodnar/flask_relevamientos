from functools import wraps
from flask import session, request, redirect, url_for

# Comprueba logueo
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('username') is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# Comprueba directivo
def directivo_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('level') not in (0, 10):
            return redirect(url_for('formularios', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


# Comprueba admin
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('level') != 0:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
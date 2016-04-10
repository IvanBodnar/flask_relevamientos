from relevamientos.app import app, db
from flask import render_template, flash, redirect, url_for, request
from formularios.forms import Formulario1Form
from formularios.models import Formulario1
from relevamientos.decorators import login_required, directivo_required, admin_required
from maps.models import Calles
import json
import requests

GOOGLE_KEY = 'AIzaSyBKUvzwTGE65RwwhrXa67pFfF3PkvynMSY'

@app.route('/formularios')
@login_required
def formularios():
    return render_template('formularios/formularios.html')


@app.route('/formulario1', methods=('GET', 'POST'))
@login_required
def formulario1():
    form = Formulario1Form()
    error = None
    query_calles = Calles.query.order_by(Calles.nombre).all()
    CALLES = [x.nombre for x in query_calles]

    if form.validate_on_submit():
        if not form.hora_hecho.data:
            hora_h = None
        else:
            hora_h = form.hora_hecho.data
        siniestro = Formulario1(
            hora_hecho=hora_h,
            vehiculo1=form.vehiculo1.data.lower(),
            vehiculo2=form.vehiculo2.data.lower(),
            vehiculo3=form.vehiculo3.data.lower(),
            vehiculo4=form.vehiculo4.data.lower(),
            causa=form.causa.data.lower(),
            heridos=form.heridos.data,
            obitos=form.obitos.data,
            observaciones=form.observaciones.data.lower(),
            calle1=form.calle1.data.strip().lower(),
            calle2=form.calle2.data.strip().lower(),
            altura=form.altura.data,
            lat=form.lat.data,
            long=form.long.data,
            precision=form.precision.data
        )
        try:
            db.session.add(siniestro)
            db.session.commit()
            return redirect(url_for('agregado', next=request.url))
        except:
            error = 'Dato no agregado'

    return render_template('formularios/formulario1.html', form=form, error=error, calles=json.dumps(CALLES))


@app.route('/agregado')
@login_required
def agregado():
    return render_template('formularios/agregado.html')


@app.route('/tabla')
@login_required
@directivo_required
def tabla():
    query = db.session.query(Formulario1).all()
    return render_template('formularios/tabla.html', query=query)


@app.route('/tabla_admin')
@login_required
@admin_required
def tabla_admin():
    query = db.session.query(Formulario1).all()
    return render_template('formularios/tabla_admin.html', query=query)


@app.route('/geo_gm', methods=('GET', 'POST'))
def geo_gm():
    calle1 = request.form['calle1']
    calle2 = request.form['calle2']
    altura = request.form['altura']

    if calle1 and calle2:
        address = '{}+y+{},+CABA,+AR'.format(calle1, calle2)
    elif calle1 and altura:
        address = '{}+{},+CABA,+AR'.format(calle1, altura)

    url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(address, GOOGLE_KEY)
    response = requests.get(url)
    result = response.json()
    return json.dumps(result['results'][0]['geometry']['location'])


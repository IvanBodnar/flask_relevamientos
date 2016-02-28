from relevamientos.app import app, db
from flask import render_template, flash, redirect, url_for, request
from formularios.forms import Formulario1Form
from formularios.models import Formulario1
from relevamientos.decorators import login_required
from maps.models import Calles
import json


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
        siniestro = Formulario1(
            vehiculo1=form.vehiculo1.data.lower(),
            vehiculo2=form.vehiculo2.data.lower(),
            causa=form.causa.data.lower(),
            heridos=form.heridos.data,
            obitos=form.obitos.data,
            observaciones=form.observaciones.data.lower(),
            calle1=form.calle1.data.lower(),
            calle2=form.calle2.data.lower(),
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
def tabla():
    query = db.session.query(Formulario1).all()
    return render_template('formularios/tabla.html', query=query)


from relevamientos.app import app, db
from flask import render_template, flash, redirect, url_for, request
from formularios.forms import Formulario1Form
from formularios.models import Formulario1
from relevamientos.decorators import login_required


@app.route('/formularios')
@login_required
def formularios():
    return render_template('formularios/formularios.html')


@app.route('/formulario1', methods=('GET', 'POST'))
@login_required
def formulario1():
    form = Formulario1Form()
    error = None

    if form.validate_on_submit():
        siniestro = Formulario1(
            vehiculo1=form.vehiculo1.data,
            vehiculo2=form.vehiculo2.data,
            causa=form.causa.data,
            heridos=form.heridos.data,
            observaciones=form.observaciones.data,
            lat=form.lat.data,
            long=form.long.data
        )
        try:
            db.session.add(siniestro)
            db.session.commit()
            return redirect(url_for('agregado', next=request.url))
        except:
            error = 'Dato no agregado: %s' % form.lat.data

    return render_template('formularios/formulario1.html', form=form, error=error)


@app.route('/agregado')
@login_required
def agregado():
    return render_template('formularios/agregado.html')


@app.route('/tabla')
@login_required
def tabla():
    query = db.session.query(Formulario1).all()
    return render_template('formularios/tabla.html', query=query)

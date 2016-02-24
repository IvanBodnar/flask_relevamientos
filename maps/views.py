from relevamientos.app import app
from flask import render_template
from relevamientos.decorators import login_required
from formularios.models import Formulario1
from geojson import Feature, Point, FeatureCollection



@app.route('/mapa')
@login_required
def mapa():
    query = Formulario1.query.all()
    point_list = []
    for item in query:
        try:
            long_lat = (float(item.long), float(item.lat))
        except:
            long_lat = (0.0, 0.0)
        vehiculo1 = item.vehiculo1
        vehiculo2 = item.vehiculo2
        causa = item.causa.capitalize()
        heridos = item.heridos
        point = Point(long_lat)

        feature = Feature(geometry=point,
                          properties={'causa': causa, 'vehiculo1':vehiculo1,
                                     'vehiculo2': vehiculo2, 'heridos': heridos})

        point_list.append(feature)
    geo_json = FeatureCollection(point_list)

    return render_template('maps/mapa.html', geo_json=geo_json)


from flask import request
import json
import requests

GOOGLE_KEY = 'AIzaSyBKUvzwTGE65RwwhrXa67pFfF3PkvynMSY'

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
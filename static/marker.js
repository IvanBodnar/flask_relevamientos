


function onEachFeature(feature, layer) {
    if (feature.properties) {
        var ft = feature.properties;
        layer.bindPopup(ft.causa.bold().fontcolor('red').fontsize(3) + '<br>'
                        + 'Involucrado 1: ' + ft.vehiculo1.toUpperCase().fontcolor('red') + '<br>'
                        + 'Involucrado 2: ' + ft.vehiculo2.toUpperCase().fontcolor('red') + '<br>'
                        + 'Heridos: ' + ft.heridos.toString().fontcolor('red') + '<br>');
    }
};

var gs = document.getElementById('geo').value;
//console.log(gs)

// Parse to JSON
gs = JSON.parse(gs)

L.geoJson(gs, {
    onEachFeature: onEachFeature
}).addTo(map);





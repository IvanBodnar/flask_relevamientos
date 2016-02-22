
var gs = document.getElementById('geo').value;
console.log(gs)

L.geoJson(JSON.parse(gs)).addTo(map);





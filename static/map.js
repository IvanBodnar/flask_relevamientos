
var map = L.map('map').setView([-34.615715, -58.451204], 14);
mapLink = '<a href="http://openstreetmap.org">OpenStreetMap</a>';

L.tileLayer(
    'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy: ' + mapLink,
    maxZoom: 18
    }).addTo(map);







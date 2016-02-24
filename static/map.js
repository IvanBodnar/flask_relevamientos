// OSM code
/*
var map = L.map('map').setView([-34.615715, -58.451204], 11);
mapLink = '<a href="http://openstreetmap.org">OpenStreetMap</a>';

L.tileLayer(
    'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy: ' + mapLink,
    maxZoom: 18
    }).addTo(map);
*/


// Mapbox code
var map = L.map('map').setView([-34.615715, -58.451204], 12);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    id: 'ivangbodnar.p7n41boc',
    accessToken: 'pk.eyJ1IjoiaXZhbmdib2RuYXIiLCJhIjoiY2lnaXR0YzVvMDAwNXVha3JsZnFlZzBjbyJ9.X17WT4iMx_powofqtqKkDg'
}).addTo(map);






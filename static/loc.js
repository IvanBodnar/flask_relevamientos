var x = document.getElementById("demo");

var dummy = function(){
};

function watchLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(dummy);
    } else {
        alert("Geolocalización no soportada en este navegador");
    }
}

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position, dummy, {maximumAge:600000, timeout:5000, enableHighAccuracy: true});
    } else {
        alert("Geolocalización no soportada en este navegador");
    }
}

function position(position) {
    document.getElementById('Lat').value = position.coords.latitude.toFixed(8);
    document.getElementById('Long').value = position.coords.longitude.toFixed(8);
    document.getElementById('Precision').value = position.coords.accuracy.toFixed(2);
}

window.onload = function() {
    watchLocation();
};
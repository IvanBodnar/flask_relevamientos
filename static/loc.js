var x = document.getElementById("demo");

var dummy = function(position){
};

function startGps() {
    if (navigator.geolocation) {
        navigator.geolocation.watchPosition(dummy);
    } else {
        alert("Geolocalización no soportada en este navegador");
    }
}

function stopGps() {
    navigator.geolocation.clearWatch(startGps);
    console.log('stop');
};

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position);
    } else {
        alert("Geolocalización no soportada en este navegador");
    }
}

function position(position) {
    document.getElementById('Lat').value = position.coords.latitude.toFixed(8);
    document.getElementById('Long').value = position.coords.longitude.toFixed(8);
    document.getElementById('Precision').value = position.coords.accuracy.toFixed(2);
}

$( '#gps-btn' ).click(function() {
    startGps();
});
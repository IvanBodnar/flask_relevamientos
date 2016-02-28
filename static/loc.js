var x = document.getElementById("demo");

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function position(position) {
    document.getElementById('Lat').value = position.coords.latitude.toFixed(8);
    document.getElementById('Long').value = position.coords.longitude.toFixed(8);
    document.getElementById('Precision').value = position.coords.accuracy.toFixed(2);
}
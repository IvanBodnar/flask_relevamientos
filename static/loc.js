var x = document.getElementById("demo");

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function position(position) {
    document.getElementById('Lat').value = position.coords.latitude;
    document.getElementById('Long').value = position.coords.longitude;
}
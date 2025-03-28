// default coordinates
var map = L.map("map", {
  center: [-23.5475, -46.63611],
  zoom: 13,
  inertia: true
});
  // add OpenStreetMap tiles to the map
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);


// set the new coordinates when the user enters new values in the input fields
function setCoordinates(){
    let longitude = document.getElementById("longitudeInput").value;
    let latitude = document.getElementById("latitudeInput").value;

    longitude = parseFloat(longitude);
    latitude = parseFloat(latitude);

    L.marker().closePopup();
    
    var coordinates = [latitude, longitude];
    L.marker(coordinates).addTo(map);
    map.panTo(coordinates);
}
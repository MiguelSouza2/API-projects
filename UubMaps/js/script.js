var map = L.map("map", {
  center: [-23.5475, -46.63611],
  zoom: 13,
});

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

L.marker([-23.55052, -46.633308])
  .addTo(map)
  .bindPopup("Essa é a cidade de São Paulo")
  .openPopup();

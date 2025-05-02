latitude = -24.5002295;
longitude = -47.8448116;

const map = new ol.Map({
  layers: [
    new ol.layer.Tile({
      source: new ol.source.TileJSON({
        url: "https://api.maptiler.com/maps/satellite/tiles.json?key=jJl02mktrOXOYRHoD7Gi",
        tileSize: 512
    })
  })
],

  target: 'map',
  view: new ol.View({
    center: ol.proj.fromLonLat([-47.8448116, -24.5002295]),
    zoom: 13

  })
});
import './style.css';
import {Map, View} from 'ol';
import TileLayer from 'ol/layer/Tile';
import {OSM, Vector as VectorSource} from 'ol/source.js';
import JSONFeature from 'ol/format/JSONFeature.js';
import {tile as tileStrategy} from 'ol/loadingstrategy.js';
import {createXYZ} from 'ol/tilegrid.js';
// console.log("aaaaaaaaaaaaaaa");
// import require from 'request';
// console.log("bbbbbbbbbbbbb");

const REST_URL = 'http://localhost:8000/api?linha=433'

const map = new Map({
  target: 'map',
  layers: [
    new TileLayer({
      source: new OSM()
    })
  ],
  view: new View({
    center: [0, 0],
    zoom: 2
  })
});

const vectorSource = new VectorSource({
  format: new JSONFeature(),
  url: function (extent, resolution, projection) {
    // ArcGIS Server only wants the numeric portion of the projection ID.
    console.log("aaaaaaaaaa",extent);
    const srid = projection
      .getCode()
      .split(/:(?=\d+$)/)
      .pop();

    const url = REST_URL;

    return url;
  },
  strategy: tileStrategy(
    createXYZ({
      tileSize: 512,
    })
  )
});

// var request = require('request');
// console.log('============');
// request(REST_URL, function (error, response, body) {
//   console.log('error:', error); // Print the error if one occurred
//   console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
//   console.log('body:', body); // Print the HTML for the Google homepage.
// });
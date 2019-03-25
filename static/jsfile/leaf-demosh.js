



var map = L.map( 'map', {
    center: [25.3084, 82.9025],
    minZoom: 2,
    zoom: 11,
});

L.tileLayer( 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    subdomains: ['a','b','c']
}).addTo( map );


function route() {
//var vehicle=$('#vehicle_s').val()+$('#vehicle_number').val();
var car=$('#vehicle').val();
var choice=$('#datepicker-1').val();




var i=0;
  $.ajax({
   url: '/app/data_pah/',
    type: 'GET',
    dataType: 'json',
    data:{'vehicle': car,
          'choice':choice,
         },


  })
  .done(function(data) {

var no_of_vehicle = Object.keys(data).length;
console.log(no_of_vehicle);
var myURL = jQuery( 'script[src$="leaf-demosh.js"]' ).attr( 'src' ).replace( 'leaf-demosh.js', '' );
var myIcon1 = L.icon({
   iconUrl: '../static/img/g2.png',
  iconRetinaUrl:'../static/img/g2.png',
  iconSize: [29, 24],
  iconAnchor: [9, 21],
  popupAnchor: [0, -14]
});

var myIconRed = L.icon({
   iconUrl: '../static/img/r2.png',
  iconRetinaUrl:'../static/img/r2.png',
  iconSize: [29, 24],
  iconAnchor: [9, 21],
  popupAnchor: [0, -14]
});


console.log(data);
for(var j=0;j<no_of_vehicle;j++)
{
var length=Object.keys(data[j]).length;
console.log(length);
if(length>0)
{
var mid=parseInt((length-1)/2)
map.setView([data[0][Object.keys(data[0]).length-1].latitude, data[0][Object.keys(data[0]).length-1].longitude], 13);




for(var i=0;i< length-1;i++)
{


//console.log(data[j][i].longitude);



var pointA = new L.LatLng(data[j][i].latitude, data[j][i].longitude);
    var pointB = new L.LatLng(data[j][i+1].latitude, data[j][i+1].longitude);




var pointList = [pointA, pointB];

var firstpolyline = new L.Polyline(pointList, {
    color: 'green',
    weight: 5,
    opacity: 0.5,
    smoothFactor: 2
});
firstpolyline.addTo(map);





}





var htmls = `
        <div>
          <span>vehicle Number: <b>` + data[j][0].vehicle_number+ `</b></span><br>
          <span>Driver Name: <b>`+ data[j][0].driver+ `</b></span><br>
          <span>Last Location: <b>`+ data[j][0].place+`</b></span><br>
          <span>Updated At: <b>`+ data[j][0].time_recorded + `</b></span><br>
        </div> `
L.marker( [data[j][0].latitude, data[j][0].longitude], {icon: myIconRed} )
      .bindPopup( htmls )
      .addTo( map );



 var htmle = `
        <div>
          <span>vehicle Number: <b>` + data[j][length-1].vehicle_number+ `</b></span><br>
          <span>Driver Name: <b>`+ data[j][length-1].driver+ `</b></span><br>
          <span>Last Location: <b>`+ data[j][length-1].place +`</b></span><br>
          <span>Updated At: <b>`+ data[j][length-1].time_recorded + `</b></span><br>
        </div>`

L.marker( [data[j][length-1].latitude, data[j][length-1].longitude], {icon: myIcon1} )
      .bindPopup( htmle )
      .addTo( map );




}
}


  })





  .fail(function() {
    console.log("error");
  })
  .always(function() {
    console.log("complete");
  });

 }

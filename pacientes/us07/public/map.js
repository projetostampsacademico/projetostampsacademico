function myMap() {

    if (navigator.geolocation) {
         navigator.geolocation.getCurrentPosition(function(position) {

             var jsonpadrao = {
                 data: []
             };

             var dadoJson = {};

             dadoJson.lat = position.coords.latitude - 0.001;
             dadoJson.lon = position.coords.longitude - 0.001;

             jsonpadrao.data.push(dadoJson);

             console.log(JSON.stringify(jsonpadrao));

             var mapOptions = {
                 center: new google.maps.LatLng(position.coords.latitude, position.coords.longitude),
                 zoom: 15,
                 mapTypeId: google.maps.MapTypeId.HYBRID,
             };
             var map = new google.maps.Map(document.getElementById("map"), mapOptions);
             // Display multiple markers on a map
             var infowindow = new google.maps.InfoWindow();

             var marker = new google.maps.Marker({
                 position: new google.maps.LatLng(position.coords.latitude - 0.000, position.coords.longitude - 0.000),
                 map: map,
                 title: "Você está aqui!"
             });
             infowindow.setContent("Você está aqui!");
             infowindow.open(map, marker);

             google.maps.event.addListener(marker, 'click', (function(marker, i) {
                 return function() {
                     infowindow.setContent("Você está aqui!");
                     infowindow.open(map, marker);
                 }
             })(marker, i));


             for (var i = 0; i < jsonpadrao.data.length; i++) {
                 var pos = new google.maps.LatLng(jsonpadrao.data[i].lat, jsonpadrao.data[i].lon);
                 var marker =  new google.maps.Marker({
                     position: pos,
                     map: map,
                     title: i
                 });
                 google.maps.event.addListener(marker, 'click', (function(marker, i) {
                     return function() {
                         infowindow.setContent("TESTE: " + i);
                         infowindow.open(map, marker);
                     }
                 })(marker, i));
             }
         });
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}
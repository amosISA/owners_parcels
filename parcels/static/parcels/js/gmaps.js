var mapa = null;
var oldmap = null;
function loadMap(){
    var alicante = new google.maps.LatLng(38.345628,-0.480759);
    var myOptions = {
        zoom: 17,
        center: alicante,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    mapa = new google.maps.Map(document.getElementById('map_canvas'), myOptions);

    //AQUÍ INDICAMOS LOS EVENTOS QUE ESCUHARÁ EL MAPA
    google.maps.event.addListener(mapa, 'dragend',
        function(){
            overlay()
        }
    )

    google.maps.event.addListener(mapa, 'zoom_changed',
        function(){
            overlay()
        }
    )

    google.maps.event.addListenerOnce(mapa, 'tilesloaded',
        function(){
            overlay()
        }
    ) //Sólo me interesa tenerlo cuando se carga el mapa por primera vez
}

//Esta función introduce la imagen del Catastro en el mapa
function overlay(){
    var bounds = mapa.getBounds()
    var ne = bounds.getNorthEast()
    var sw = bounds.getSouthWest()

    if(oldmap != null){
        oldmap.setMap(null)  //'Despinta' la imagen anterior para que no se solapen mucho
        oldmap = null
    }

    oldmap = new google.maps.GroundOverlay("http://ovc.catastro.meh.es/Cartografia/WMS/ServidorWMS.aspx?SERVICE=WMS&SRS=EPSG:4326&REQUEST=GETMAP&bbox="+sw.lng()+","+sw.lat()+","+ne.lng()+","+ne.lat()+"&width=640&height=480&format=PNG&transparent=Yes&layers=catastro" , mapa.getBounds());
    oldmap.setMap(mapa);
}
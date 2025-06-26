document.addEventListener('DOMContentLoaded', function() {
    const map = L.map('map').setView([23.1136, -82.3666], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
    
    const marker = L.marker([23.1136, -82.3666], {draggable: true}).addTo(map);
    const latField = document.querySelector('[name="latitude"]');
    const lngField = document.querySelector('[name="longitude"]');
    
    marker.on('dragend', function(e) {
        const latLng = e.target.getLatLng();
        latField.value = latLng.lat;
        lngField.value = latLng.lng;
    });
    
    document.getElementById('location-btn').addEventListener('click', function() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                const lat = position.coords.latitude;
                const lng = position.coords.longitude;
                
                map.setView([lat, lng], 15);
                marker.setLatLng([lat, lng]);
                
                latField.value = lat;
                lngField.value = lng;
            });
        } else {
            alert("Tu navegador no soporta geolocalización");
        }
    });
    
    document.querySelector('form').addEventListener('submit', function(e) {
        if (!latField.value || !lngField.value) {
            e.preventDefault();
            alert("Debes seleccionar una ubicación en el mapa");
        }
    });
});
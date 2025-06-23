document.addEventListener('DOMContentLoaded', function() {
    const map = L.map('map').setView([23.1136, -82.3666], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
    
    const marker = L.marker([23.1136, -82.3666], {draggable: true}).addTo(map);
    
    const latitudeField = document.querySelector('[name="latitude"]');
    const longitudeField = document.querySelector('[name="longitude"]');
    
    marker.on('dragend', function(e) {
        const latLng = e.target.getLatLng();
        latitudeField.value = latLng.lat.toFixed(6);
        longitudeField.value = latLng.lng.toFixed(6);
    });
    
    document.getElementById('location-btn').addEventListener('click', function() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                const lat = position.coords.latitude;
                const lng = position.coords.longitude;
                
                map.setView([lat, lng], 15);
                marker.setLatLng([lat, lng]);
                
                latitudeField.value = lat.toFixed(6);
                longitudeField.value = lng.toFixed(6);
            });
        } else {
            alert("Tu navegador no soporta geolocalización");
        }
    });
    
    document.querySelector('form').addEventListener('submit', function(e) {
        if (!latitudeField.value || !longitudeField.value) {
            e.preventDefault();
            alert("Debes seleccionar una ubicación en el mapa");
        }
    });
});
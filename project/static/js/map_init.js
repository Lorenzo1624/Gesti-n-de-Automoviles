// Versión 3.0 - Solución completa
function initMap(map, options) {
    // Verificación extrema de parámetros
    if (!map || typeof map.setView !== 'function') {
        console.error('Error: Objeto de mapa inválido', map);
        return;
    }

    if (!options || typeof options !== 'object') {
        console.error('Error: Opciones inválidas', options);
        return;
    }

    // Obtener coordenadas de tres formas diferentes
    const getCoordinates = () => {
        // 1. Desde options (si django-leaflet las pasa)
        if (options.lat && options.lng) {
            return {
                lat: parseFloat(options.lat),
                lng: parseFloat(options.lng)
            };
        }

        // 2. Desde dataset del contenedor
        const container = document.getElementById(options.mapid);
        if (container && container.dataset) {
            const lat = parseFloat(container.dataset.lat);
            const lng = parseFloat(container.dataset.lng);
            if (!isNaN(lat) && !isNaN(lng)) {
                return { lat, lng };
            }
        }

        // 3. Valores por defecto (México)
        return {
            lat: 23.6345,
            lng: -102.5528
        };
    };

    const { lat, lng } = getCoordinates();
    console.log('Coordenadas finales:', lat, lng);

    // Configuración del mapa
    try {
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap'
        }).addTo(map);

        map.setView([lat, lng], 15);
        
        L.marker([lat, lng])
            .addTo(map)
            .bindPopup("Ubicación del vehículo")
            .openPopup();
    } catch (e) {
        console.error('Error al configurar el mapa:', e);
    }
}

// Registro seguro del callback
if (typeof window !== 'undefined') {
    window.initMap = initMap;
} else {
    console.error('El objeto window no está disponible');
}
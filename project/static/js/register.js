document.addEventListener('DOMContentLoaded', function() {
   
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(e) {
            const terms = document.getElementById('terms');
            if (!terms.checked) {
                e.preventDefault();
                alert('Debes aceptar los términos y condiciones');
                terms.focus();
            }
        });
    }
});
document.addEventListener('DOMContentLoaded', () => {
    const openPopupBtn = document.getElementById('calidadAire');
    const closePopupBtn = document.getElementById('closePopupBtn');
    const popup = document.getElementById('popup');
    const popupContent = document.getElementById('popupContent');

    openPopupBtn.addEventListener('click', async () => {
        popup.style.display = 'block';
        try {
            const response = await fetch('./tables/datosAire.html'); // URL del API
            if (response.ok) {
                const data = await response.text();
                popupContent.innerHTML = data;
            } else {
                popupContent.innerHTML = 'Error al cargar el contenido.';
            }
        } catch (error) {

            console.error(error)
            popupContent.innerHTML = 'Error al realizar la solicitud.';
        }
    });

    closePopupBtn.addEventListener('click', () => {
        popup.style.display = 'none';
    });

    
    window.addEventListener('click', (event) => {
        if (event.target == popup) {
            popup.style.display = 'none';
        }
    });
});
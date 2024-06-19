// Esperar a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', () => {
    // Obtener referencia al campo de documento
    const documentoInput = document.getElementById('documento');
    // Manejador de evento para validar número de documento
    documentoInput.addEventListener('blur', async () => {
        const value = documentoInput.value.trim();
        if (value === '') return; // No hacer nada si está vacío
        try {
            // Realizar una solicitud a tu backend para verificar si el documento ya existe
            const response = await fetch(`/verificar_documento/${encodeURIComponent(value)}`);
            if (!response.ok) {
                throw new Error('Error al verificar el número de documento.');
            }
            const data = await response.json();
            if (data.existe) {
                documentoInput.classList.add('is-invalid');
                document.getElementById('documentoError').textContent = '¡Este número de documento ya ha sido registrado!';
            } else {
                documentoInput.classList.remove('is-invalid');
                document.getElementById('documentoError').textContent = '';
            }
        } catch (error) {
            console.error('Error:', error);
            // Manejar el error, por ejemplo, mostrando un mensaje genérico
            documentoInput.classList.add('is-invalid');
            document.getElementById('documentoError').textContent = 'Error al verificar el número de documento.';
        }
    });
});

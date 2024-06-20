const $formulario = document.getElementById('formulario');
const $documento = document.getElementById('documento');

(function () {
    // Simula una función que verifica si el documento ya existe
    function documentoExiste(documento) {
        // Aquí deberías implementar la lógica para verificar en tu base de datos o lista
        // Esta es una función de ejemplo que siempre devuelve falso
        return false;
    }

    $formulario.addEventListener('submit', function (e) {
        let documentoValor = $documento.value.trim(); // Obtener el valor del documento y quitar espacios en blanco

        if (documentoExiste(documentoValor)) {
            alert("Ya existe este documento.");
            e.preventDefault(); // Detener el envío del formulario si el documento ya existe
        }
    });
})();

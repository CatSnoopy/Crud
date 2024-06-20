const $formulario = document.getElementById('formulario');
const $documento = document.getElementById('documento');

(function () {
    $formulario.addEventListener('submit', function (e) {
        let documento = String($documento.value);
        if (documento.repeat) {
            alert("ya existe este documento ")
            e.preventDefault();
        }

    })
})();
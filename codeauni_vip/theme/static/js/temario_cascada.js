document.addEventListener("DOMContentLoaded", function () {
    // Seleccionamos los combos por ID (Django Admin usa id_<nombre_campo>)
    const cursoSelect = document.querySelector("#id_curso");
    const moduloSelect = document.querySelector("#id_tipo_modulo");

    if (cursoSelect && moduloSelect) {
        cursoSelect.addEventListener("change", function () {
            let cursoId = this.value;

            fetch(`/ajax/cargar-modulos/?curso_id=${cursoId}`)
                .then(response => response.json())
                .then(data => {
                    moduloSelect.innerHTML = "";
                    data.forEach(function (modulo) {
                        let option = new Option(modulo.nombre_modulo, modulo.id);
                        moduloSelect.add(option);
                    });
                });
        });
    }
});

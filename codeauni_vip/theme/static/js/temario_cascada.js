document.addEventListener("DOMContentLoaded", () => {
    const cursoSelect = document.querySelector("#id_curso");
    const moduloSelect = document.querySelector("#id_tipo_modulo");

    if (!cursoSelect || !moduloSelect) return;

    function setModuloOptions(modulos, previousSelectedValue) {
        const optionsHtml = `
            <option value="">---------</option>
            ${modulos.map(modulo => {
                const isSelected = String(previousSelectedValue) === String(modulo.id) ? 'selected' : '';
                return `<option value="${modulo.id}" ${isSelected}>${modulo.nombre_modulo}</option>`;
            }).join('')}
        `;
        moduloSelect.innerHTML = optionsHtml;
        moduloSelect.disabled = modulos.length === 0;

        if (previousSelectedValue && !modulos.some(m => String(m.id) === String(previousSelectedValue))) {
            moduloSelect.value = "";
        }
    }

    async function cargarModulos(cursoId) {
        const previousSelected = moduloSelect.value;
        if (!cursoId) {
            setModuloOptions([], null);
            return;
        }

        try {
            const response = await fetch(`/ajax/cargar-modulos/?curso_id=${encodeURIComponent(cursoId)}`);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            setModuloOptions(data, previousSelected);
        } catch (e) {
            console.error("Error al cargar módulos:", e);
            setModuloOptions([], null);
        }
    }

    cargarModulos(cursoSelect.value);

    const eventsToListen = ["change", "select2:select", "select2:clear", "select2:unselect"];
    eventsToListen.forEach(event => {
        cursoSelect.addEventListener(event, () => cargarModulos(cursoSelect.value));
    });

    try {
        if (window.django && window.django.jQuery) {
            window.django.jQuery(document).on(eventsToListen.slice(1).join(' '), "#id_curso", function () {
                cargarModulos(this.value);
            });
        }
    } catch (e) {
    }
});
console.log("🚀 Script condicional cargado en admin");

document.addEventListener('DOMContentLoaded', function () {
    const tipoEntrega = document.getElementById('id_tipo_entrega');
    const tipoContenido = document.getElementById('id_tipo_contenido')?.closest('.form-row') || document.getElementById('id_tipo_contenido')?.closest('.field');
    const diasDisponibles = document.getElementById('id_dias_disponibles')?.closest('.form-row') || document.getElementById('id_dias_disponibles')?.closest('.field');

    function toggleCampos() {
        const valor = tipoEntrega.value;

        if (valor === 'ondemand') {
            if (tipoContenido) tipoContenido.style.display = '';
            if (diasDisponibles) diasDisponibles.style.display = 'none';
        } else if (valor === 'envivo') {
            if (tipoContenido) tipoContenido.style.display = 'none';
            if (diasDisponibles) diasDisponibles.style.display = '';
        } else {
            if (tipoContenido) tipoContenido.style.display = 'none';
            if (diasDisponibles) diasDisponibles.style.display = 'none';
        }
    }

    if (tipoEntrega) {
        tipoEntrega.addEventListener('change', toggleCampos);
        toggleCampos();  // Ejecutar al cargar
    }
});

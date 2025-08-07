function openFormPayment(tipo = 'estudiante') {
  let formSubmitted = false;

  const precios = {
    estudiante: {
      label: 'Estudiante',
      detalles: [
        '1 Membresía Estudiante $149.90/año',
        '2 Membresías Estudiante $269.82/año',
        '3 Membresías Estudiante $359.76/año'
      ],
      endpoint: '/api/guardar-formulario/'
    },
    profesional: {
      label: 'Profesional',
      detalles: [
        '1 Membresía Profesional $249.90/año',
        '2 Membresías Profesional $449.82/año',
        '3 Membresías Profesional $599.76/año'
      ],
      endpoint: '/api/guardar-formulario-profesional/'
    }
  };

  const datos = precios[tipo] || precios.estudiante;

  Swal.fire({
    title: ' ',
    width: '28rem',
    showCloseButton: true,
    showConfirmButton: false,
    allowOutsideClick: true,
    html: `
      <form id="vip-form" class="text-left text-sm text-black space-y-4 font-sans">

        <h2 class="text-center text-lg font-semibold">Selecciona tu membresía (${datos.label})</h2>

        <div class="space-y-3">
          ${datos.detalles.map((detalle, index) => `
            <label class="relative flex flex-col justify-center items-center border-2 rounded-xl px-4 py-3 cursor-pointer text-center peer-checked:bg-blue-100 peer-checked:ring-2 peer-checked:ring-blue-300 transition-all border-[#00D2FF]">
              <input type="radio" name="membresia" value="${index + 1}" class="hidden peer" ${index === 0 ? 'required' : ''}>
              <span class="text-[32px] font-bold leading-none text-black">${index + 1} Membresía</span>
              <span class="text-[16px] text-gray-600 font-medium">CODEa VIP</span>
              ${index > 0 ? `<span class="absolute top-2 right-3 bg-cyan-400 text-black text-xs font-semibold px-2 py-0.5 rounded-md">${index * 10}%Off</span>` : ''}
            </label>
          `).join('')}
        </div>

        <div>Detalles:
          <p id="detalles-membresia">${datos.detalles[0]}</p>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <input name="nombre" placeholder="Nombre" class="border rounded-md px-3 py-2 w-full" required />
          <input name="apellido" placeholder="Apellido" class="border rounded-md px-3 py-2 w-full" required />
        </div>

        <div class="flex gap-2">
          <input name="telefono" placeholder="Teléfono" class="border rounded-md px-3 py-2 w-full" required />
        </div>

        <input name="correo" placeholder="Correo electrónico" class="border rounded-md px-3 py-2 w-full" required />
        <input name="pais" placeholder="País" class="border rounded-md px-3 py-2 w-full" required />

        <select name="especializacion" class="border rounded-md px-3 py-2 w-full text-gray-600" required>
          <option value="" disabled selected>Especialización</option>
          <option value="Minería">Minería</option>
          <option value="Ingeniería">Ingeniería</option>
          <option value="Metalurgia">Metalurgia</option>
          <option value="Mantenimiento">Mantenimiento</option>
          <option value="Afines">Afines</option>
        </select>

        <button type="submit" class="w-full bg-[#0068FF] text-white py-2 rounded-md font-semibold mt-4 hover:bg-[#0053cc]">
          Contactar asesor
        </button>
      </form>

      <div id="membresia-detalle" class="mt-4 text-center hidden">
        <p id="detalle-membresia-seleccionada" class="font-semibold"></p>
      </div>
    `,

    didOpen: () => {
      const form = document.getElementById('vip-form');
      const detallesMembresia = document.getElementById('detalles-membresia');
      const detalleMembresiaSeleccionada = document.getElementById('detalle-membresia-seleccionada');
      const membresiaDetalle = document.getElementById('membresia-detalle');

      form.querySelectorAll('input[name="membresia"]').forEach(radio => {
        radio.addEventListener('change', () => {
          detallesMembresia.textContent = datos.detalles[parseInt(radio.value) - 1];
        });
      });

      form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const data = Object.fromEntries(new FormData(form).entries());

        if (Object.values(data).some(value => !value)) {
          Swal.showValidationMessage('Por favor completa todos los campos');
          return;
        }

        membresiaDetalle.classList.remove('hidden');
        const detalleSeleccionado = datos.detalles[parseInt(data.membresia) - 1];
        detalleMembresiaSeleccionada.textContent = `${detalleSeleccionado}`;

        const mensaje = `Hola, mi nombre es ${data.nombre} ${data.apellido}.
        Quiero comprar ${detalleSeleccionado}.
        Soy de ${data.pais}, mi correo es ${data.correo}, me especializo en ${data.especializacion}.`;

        const telefonoDestino = '51919543397';
        const url = `https://wa.me/${telefonoDestino}?text=${encodeURIComponent(mensaje)}`;
        window.open(url, '_blank');

        await fetch(datos.endpoint, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data)
        });

        formSubmitted = true;
        Swal.close();
      });
    },

    didClose: () => {
      if (!formSubmitted && typeof window.openFormFree2 === 'function') {
        window.openFormFree2();
      }
    }
  });
}

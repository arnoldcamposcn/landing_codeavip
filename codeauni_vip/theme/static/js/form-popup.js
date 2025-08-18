function openFormPayment(tipo = 'estudiante', precio_base) {
  let formSubmitted = false;

  const precios = {
    estudiante: {
      label: 'Estudiante',
      detalles: function() {
        const precio1 = precio_base;
        const precio2 = (precio_base * 2) * 0.9;  // 10% descuento
        const precio3 = (precio_base * 3) * 0.8;  // 20% descuento
        
        return [
          `1 Membresía Estudiante $${precio1.toFixed(2)}/año`,
          `2 Membresías Estudiante $${precio2.toFixed(2)}/año`,
          `3 Membresías Estudiante $${precio3.toFixed(2)}/año`
        ]
      },
      endpoint: '/api/guardar-formulario/'
    },
    profesional: {
      label: 'Profesional',
      detalles: function() {

        const precio1 = parseFloat(precio_base);
        const precio2 = (precio1 * 2) * 0.9; 
        const precio3 = (precio1 * 3) * 0.8; 
        
        return [
          `1 Membresía Profesional $${precio1.toFixed(2)}/año`,
          `2 Membresías Profesional $${precio2.toFixed(2)}/año`,
          `3 Membresías Profesional $${precio3.toFixed(2)}/año`
        ]
      },
      endpoint: '/api/guardar-formulario-profesional/'
    }
  };

  const datos = precios[tipo] || precios.estudiante;
  datos.detalles = datos.detalles();

  Swal.fire({
    title: ' ',
    width: '28rem',
    showCloseButton: true,
    showConfirmButton: false,
    allowOutsideClick: true,
    html: `
      <form id="vip-form" x-data="{ selectedPlan: '1' }" class="text-left text-sm text-black space-y-4 font-sans">

        <h2 class="text-center text-lg font-semibold">Selecciona tu membresía (${datos.label})</h2>

        <div class="space-y-3">
          ${datos.detalles.map((detalle, index) => `
            <label
              class="relative flex flex-col justify-center items-center border-2 rounded-xl px-4 py-3 pb-6 cursor-pointer text-center transition-all border-[#00D2FF]
                     peer-checked:bg-blue-100 peer-checked:ring-2 peer-checked:ring-blue-300"
              :class="selectedPlan === '${index + 1}' ? 'bg-gradient-to-r from-[#0068FF] to-[#00D2FF] text-white ring-2 ring-[#7fd9ff]/60' : ''"
              @click="selectedPlan='${index + 1}'"
            >
              <input type="radio" name="membresia" value="${index + 1}" class="hidden peer" ${index === 0 ? 'required' : ''}>
              <span class="text-[32px] font-bold leading-none">${index + 1} Membresía</span>
              <span class="text-[16px] font-medium" :class="selectedPlan === '${index + 1}' ? 'text-white/90' : 'text-gray-600'">CODEa VIP</span>
              ${index > 0 ? `
                <span class="bg-[#00D2FF] text-black text-xs font-semibold px-2 py-0.5 rounded-xl border border-black/20 shadow-sm text-right pt-4">
                  ${index * 10}%Off
                </span>` : ''}
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

        <div class="flex justify-center">
          <button type="submit" class="btn-gradient text-white font-semibold px-6 md:px-6 lg:px-6 py-3 text-base cursor-pointer mx-auto block">
            Contactar asesor
          </button>
        </div>
      </form>
    `,

    didOpen: () => {
      const form = document.getElementById('vip-form');
      const detallesMembresia = document.getElementById('detalles-membresia');

      form.querySelectorAll('input[name="membresia"]').forEach(radio => {
        radio.addEventListener('change', () => {
          detallesMembresia.textContent = datos.detalles[parseInt(radio.value, 10) - 1];
        });
      });

      form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const data = Object.fromEntries(new FormData(form).entries());
        if (Object.values(data).some(value => !value)) {
          Swal.showValidationMessage('Por favor completa todos los campos');
          return;
        }

        const detalleSeleccionado = datos.detalles[parseInt(data.membresia, 10) - 1];

        const mensaje = `Estimados,  
        Mi nombre es ${data.nombre} ${data.apellido} y me especializo en ${data.especializacion}.  
        Me comunico para manifestar mi interés en **adquirir ${detalleSeleccionado} de CODEA VIP**.  

        📍 País: ${data.pais}  
        📧 Correo: ${data.correo}  

        Quedo atento(a) a su confirmación y a los pasos para completar la compra.  
        Saludos.`;

        const telefonoDestino = '51955283690';
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

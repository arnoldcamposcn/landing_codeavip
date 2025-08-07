function openFormFree() {
    Swal.fire({
      title: ' ',
      width: '28rem',
      showCloseButton: true,
      showConfirmButton: false,
      html: `
        <form id="vip-form" class="text-left text-sm text-black space-y-4 font-sans">
  
          <h2 class="text-center text-lg font-semibold">¡Completa tus datos para la prueba gratuita!</h2>
  
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
  
        form.addEventListener('submit', async (e) => {
          e.preventDefault();
          const data = Object.fromEntries(new FormData(form).entries());
  
          if (Object.values(data).some(value => !value)) {
            Swal.showValidationMessage('Por favor completa todos los campos');
            return;
          }
  
          // Construir el mensaje de WhatsApp con los detalles de la membresía
          const mensaje = `Hola, mi nombre es ${data.nombre} ${data.apellido}.
            Quiero comprar 
            Soy de ${data.pais}, mi correo es ${data.correo}, me especializo en ${data.especializacion}.
            `;
  
          const telefonoDestino = '51919543397';
          const url = `https://wa.me/${telefonoDestino}?text=${encodeURIComponent(mensaje)}`;
          window.open(url, '_blank');
  
          await fetch('/api/guardar_formulario_free/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
          });
  
          Swal.close();
        });
      window.openFormFree = openFormFree;

      }
    });
  }
  
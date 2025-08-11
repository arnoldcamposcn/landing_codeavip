function openFormBussinesFree() {
    Swal.fire({
      title: ' ',
      width: '28rem',
      showCloseButton: true,
      showConfirmButton: false,
      html: `
        <form id="bussines-form" class="text-left text-sm text-black space-y-4 font-sans">
  
          <h2 class="text-center text-lg font-semibold">¡Completa tus datos para la prueba gratuita!</h2>
  
          <input name="nombre_empresa" placeholder="Nombre de la empresa" class="border rounded-md px-3 py-2 w-full" required />
  
          <input name="nombre_encargado" placeholder="Nombre del encargado" class="border rounded-md px-3 py-2 w-full" required />
  
          <input name="sitio_web" placeholder="Sitio web" class="border rounded-md px-3 py-2 w-full" required />
  
          <input name="telefono" placeholder="Teléfono" class="border rounded-md px-3 py-2 w-full" required />
  
          <input name="correo" placeholder="Correo electrónico" class="border rounded-md px-3 py-2 w-full" required />
  
          <input name="pais" placeholder="País" class="border rounded-md px-3 py-2 w-full" required />
  
           <button type="submit" class="btn-gradient text-white font-semibold px-6 md:px-6 lg:px-6 py-3 text-base cursor-pointer mx-auto block">
          Contactar asesor
        </button>
        </form>
  
        <div id="membresia-detalle" class="mt-4 text-center hidden">
          <p id="detalle-membresia-seleccionada" class="font-semibold"></p>
        </div>
      `,
  
      didOpen: () => {
        const form = document.getElementById('bussines-form');
  
        form.addEventListener('submit', async (e) => {
          e.preventDefault();
          const data = Object.fromEntries(new FormData(form).entries());
  
          if (Object.values(data).some(value => !value)) {
            Swal.showValidationMessage('Por favor completa todos los campos');
            return;
          }
  
          // Construir el mensaje de WhatsApp para profesionales
          const mensaje = `Estimados,  
          Mi nombre es ${data.nombre_encargado}, representante de la empresa ${data.nombre_empresa}.  
          Nos gustaría solicitar una **prueba gratuita de CODEA BUSINESS**.  

          📞 Teléfono: ${data.telefono}  
          📧 Correo: ${data.correo}  
          📍 País: ${data.pais}  
          🌐 Sitio web: ${data.sitio_web}  

          Quedo atento(a) a su confirmación y a los pasos para acceder a la prueba.  
          Saludos.`;
  
          const telefonoDestino = '51955283690';
          const url = `https://wa.me/${telefonoDestino}?text=${encodeURIComponent(mensaje)}`;
          window.open(url, '_blank');
  
          await fetch('/api/free_formulario_bussines/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
          });
  
          Swal.close();
        });
        window.openFormBussines = openFormBussines;
      }
    });
  }
  
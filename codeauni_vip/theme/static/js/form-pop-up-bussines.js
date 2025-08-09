window.openFormBussines = function(selectedPlan) {
  if (!selectedPlan) {
      // Seguridad por si llaman sin seleccionar
      Swal.fire({ icon: 'warning', text: 'Selecciona un plan antes de continuar.' });
      return;
    }

    Swal.fire({
      title: ' ',
      width: '28rem',
      showCloseButton: true,
      showConfirmButton: false,
      html: `
        <form id="bussines-form" class="text-left text-sm text-black space-y-4 font-sans">
          <h2 class="text-center text-lg font-semibold">¡Completa tus datos para solicitar tu compra!</h2>

          <!-- Detalle de planes -->
          <div id="detalle-planes" class="mt-4">
            <div class="plan-box" data-plan="plan1" style="display:none">
              <!-- Caja 1 -->
              <p>Detalle:</p>
              <!-- ... tu HTML de la caja 1 tal cual ... -->
              <p class="mt-2 font-medium">Plan seleccionado: 2-10 • $200 USD x persona • 20% OFF</p>
            </div>

            <div class="plan-box" data-plan="plan2" style="display:none">
              <!-- Caja 2 -->
              <p>Detalle:</p>
              <!-- ... tu HTML de la caja 2 tal cual ... -->
              <p class="mt-2 font-medium">Plan seleccionado: 11-100 • $170 USD x persona • 25% OFF</p>
            </div>

            <div class="plan-box" data-plan="plan3" style="display:none">
              <!-- Caja 3 -->
              <p>Detalle:</p>
              <!-- ... tu HTML de la caja 3 tal cual ... -->
              <p class="mt-2 font-medium">Plan seleccionado: +100 • $150 USD x persona • 30% OFF</p>
            </div>
          </div>

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
      `,
      didOpen: () => {
        // Mostrar solo la caja del plan elegido
        document.querySelectorAll('.plan-box').forEach(box => {
          box.style.display = (box.dataset.plan === selectedPlan) ? 'block' : 'none';
        });

        const form = document.getElementById('bussines-form');
        form.addEventListener('submit', async (e) => {
          e.preventDefault();
          const data = Object.fromEntries(new FormData(form).entries());

          // Resumen del plan según selectedPlan
          const planResumen = {
            plan1: '2-10 usuarios • $200 USD x persona • 20% OFF',
            plan2: '11-100 usuarios • $170 USD x persona • 25% OFF',
            plan3: '+100 usuarios • $150 USD x persona • 30% OFF',
          }[selectedPlan];

          const mensaje = `Estimados,  
          Mi nombre es ${data.nombre_encargado}, representante de la empresa ${data.nombre_empresa}.  
          Me comunico para manifestar nuestro interés en adquirir el plan ${planResumen} CODEA BUSSINES.  
          
          📍 País: ${data.pais}  
          📞 Teléfono: ${data.telefono}  
          📧 Correo: ${data.correo}  
          🌐 Sitio web: ${data.sitio_web}  
          
          Quedo atento(a) a sus indicaciones para continuar con el proceso.  
          Saludos.`;

          const telefonoDestino = '51919543397';
          const url = `https://wa.me/${telefonoDestino}?text=${encodeURIComponent(mensaje)}`;
          window.open(url, '_blank');

          // Enviar también al backend
          await fetch('/api/guardar_formulario_bussines/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ ...data, plan: selectedPlan })
          });

          Swal.close();
        });
      }
    });
  }

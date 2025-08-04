function openForm() {
    Swal.fire({
      title: ' ',
      width: '28rem',
      showCloseButton: true,
      showConfirmButton: false,
      html: `
        <form id="vip-form" class="text-left text-sm text-black space-y-4 font-sans">
  
          <h2 class="text-center text-lg font-semibold">Selecciona tu membresía</h2>
  
          <div class="space-y-3">
            <label class="flex flex-col justify-center items-center border-2 rounded-xl px-4 py-3 cursor-pointer text-center peer-checked:bg-blue-100 transition-all border-[#00D2FF]">
            <input type="radio" name="membresia" value="1" class="hidden peer" required>
            <span class="text-[32px] font-bold leading-none text-black">1 Membresía</span>
            <span class="text-[16px] text-gray-600 font-medium">CODEa VIP</span>
            </label>

  
            <h3 class="text-center text-sm font-semibold text-gray-500 -mb-2 mt-2">¡Invita a tus amigos!</h3>
  
           <label class="relative flex flex-col justify-center items-center border-2 rounded-xl px-4 py-3 cursor-pointer text-white text-center peer-checked:bg-blue-100 peer-checked:ring-2 peer-checked:ring-blue-300 transition-all border-[#00D2FF]">
            <input type="radio" name="membresia" value="2" class="hidden peer">
            <span class="text-[32px] font-bold leading-none text-black">2 Membresía</span>
            <span class="text-[16px] font-medium text-gray-600">CODEa VIP</span>
            <span class="absolute top-2 right-3 bg-cyan-400 text-black text-xs font-semibold px-2 py-0.5 rounded-md">10%Off</span>
            </label>
  
          <label class="relative flex flex-col justify-center items-center border-2 rounded-xl px-4 py-3 cursor-pointer text-center peer-checked:bg-blue-100 peer-checked:ring-2 peer-checked:ring-blue-300 transition-all border-[#00D2FF]">
        <input type="radio" name="membresia" value="3" class="hidden peer">
        <span class="text-[32px] font-bold leading-none text-black">3 Membresía</span>
        <span class="text-[16px] text-gray-600 font-medium">CODEa VIP</span>
        <span class="absolute top-2 right-3 bg-cyan-400 text-black text-xs font-semibold px-2 py-0.5 rounded-md">20%Off</span>
        </label>

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
          </select>
  
          <div>
            <p class="font-semibold mb-1">¿Eres estudiante o profesional?</p>
            <label class="inline-flex items-center mr-4">
              <input type="radio" name="perfil" value="Estudiante" class="mr-2" required /> Estudiante
            </label>
            <label class="inline-flex items-center">
              <input type="radio" name="perfil" value="Profesional" class="mr-2" /> Profesional
            </label>
          </div>
  
          <button type="submit" class="w-full bg-[#0068FF] text-white py-2 rounded-md font-semibold mt-4 hover:bg-[#0053cc]">
            Contactar asesor
          </button>
        </form>
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
  
          const mensaje = `Hola, mi nombre es ${data.nombre} ${data.apellido}.
            Quiero comprar ${data.membresia} membresía(s).
            Soy de ${data.pais}, mi correo es ${data.correo}, soy ${data.perfil} y me especializo en ${data.especializacion}.`;

  
          const telefonoDestino = '51919543397';
          const url = `https://wa.me/${telefonoDestino}?text=${encodeURIComponent(mensaje)}`;
          window.open(url, '_blank');
  
          await fetch('/api/guardar-formulario/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
          });
  
          Swal.close();
        });
      }
    });
  }
  
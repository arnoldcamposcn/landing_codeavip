function openFormFree2() {
    Swal.fire({
      title: ' ',
      width: '28rem',
      showCloseButton: true,
      showConfirmButton: false,
      html: `
        <form id="popUpRetention" class="text-left text-sm text-black space-y-4 font-sans">
          <h2 class="text-center text-lg font-semibold">
            ¿Aún no estás listo? <br> Aprovecha hasta 3 días de prueba
          </h2>
  
          <div class="flex gap-3">
            <button id="btnPrueba" type="button" class="w-full bg-[#0068FF] text-white py-2 rounded-md font-semibold mt-4 hover:bg-[#0053cc]">
              Quiero 3 días de prueba
            </button>
  
            <button id="btnNoGracias" type="button" class="w-full bg-[#0068FF] text-white py-2 rounded-md font-semibold mt-4 hover:bg-[#0053cc]">
              No gracias
            </button>
          </div>
        </form>
  
        <div id="membresia-detalle" class="mt-4 text-center hidden">
          <p id="detalle-membresia-seleccionada" class="font-semibold"></p>
        </div>
      `,
      didOpen: () => {
        const btnNoGracias = document.getElementById('btnNoGracias');
        const btnPrueba = document.getElementById('btnPrueba');
  
        if (btnNoGracias) {
          btnNoGracias.addEventListener('click', () => {
            Swal.close();
          });
        }
  
        if (btnPrueba) {
          btnPrueba.addEventListener('click', () => {
            Swal.close();
            if (typeof window.openFormFree === 'function') {
              window.openFormFree(); 
            } else {
              console.warn('openFormFree no está definido en window');
            }
          });
        }
        window.openFormFree2 = openFormFree2;

      }
    });
  }
  
function openPopUpDescription(textoDescripcion) { 
    Swal.fire({
      title: '<span style="font-weight:600; font-size:1rem;">Descripción de la clase:</span>',
      width: '40rem',
      padding: '2rem',
      background: '#082940',
      color: '#ffffff',
      showCloseButton: true,
      showConfirmButton: false,
      html: `
        <div style="text-align:left; font-size: 0.95rem; line-height: 1.6; font-family: sans-serif;">
          ${textoDescripcion}
        </div>
      `,
    });
  }
  
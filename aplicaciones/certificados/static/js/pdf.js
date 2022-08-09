document.addEventListener("DOMContentLoaded", () => {
    // Escuchamos el click del botón
 
        const $elementoParaConvertir = document.body; // <-- Aquí puedes elegir cualquier elemento del DOM
        html2pdf()
            .set({
                margin: 1,
                filename: 'certificado-formacion.pdf',
                image: {
                    type: 'jpg',
                    quality: 1,
                },
                html2canvas: {
                    letterRendering: true,
                    scale:1,
                                 
                },
                jsPDF: {
                    unit: "px",
                    format: [1030, 800],
                    orientation: 'landscape', // landscape o portrait
                    
                }
            })
            .from($elementoParaConvertir)
            .save()
            .catch(err => console.log(err));
    ;
});


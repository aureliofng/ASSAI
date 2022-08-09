   
    document.getElementById('btnEliminacion').onclick = (e) => {   
            const confirmacion = confirm('¿Seguro que deseas eliminar esta Formación?');
            if (!confirmacion) {
                e.preventDefault();
            }
        };
   


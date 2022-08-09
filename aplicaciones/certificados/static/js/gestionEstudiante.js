   
    document.getElementById('btnEliminacion').onclick = (e) => {   
            const confirmacion = confirm('¿Seguro que deseas eliminar este Estudiante?');
            if (!confirmacion) {
                e.preventDefault();
            }
        };
   


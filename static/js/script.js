document.getElementById('userForm').addEventListener('submit', function(event) {
    const nombre = document.getElementById('nombre').value;
    const soloLetras = /^[a-zA-Z\s]+$/;

    if (!soloLetras.test(nombre)) {
        alert("Error: El nombre solo debe contener letras.");
        event.preventDefault(); // Evita que se envíe el formulario
    }
});
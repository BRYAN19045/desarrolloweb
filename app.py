from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para almacenar los datos (Simulación de base de datos)
usuarios = []

@app.route('/')
def index():
    # Renderiza el HTML y le pasa la lista de usuarios
    return render_template('index.html', usuarios=usuarios)

@app.route('/insertar', methods=['POST'])
def insertar():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        
        if nombre and correo:
            usuarios.append({'nombre': nombre, 'correo': correo})
        
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
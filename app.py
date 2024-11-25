from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    nombre = None
    total = None
    total_descuento = None

    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            edad = int(request.form['edad'])
            cantidad = int(request.form['cantidad'])


            precio_por_tarro = 9000
            total = precio_por_tarro * cantidad


            if 18 <= edad <= 30:
                descuento = 0.15
            elif edad > 30:
                descuento = 0.25
            else:
                descuento = 0.0

            total_descuento = total * (1 - descuento)
        except ValueError:

            return render_template('ejercicio1.html', error="Por favor ingresa valores válidos.")

    return render_template('ejercicio1.html', nombre=nombre, total=total, total_descuento=total_descuento)



@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    usuarios = {'juan': 'admin', 'pepe': 'user'}
    mensaje = ''

    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']


        if usuario in usuarios and usuarios[usuario] == contrasena:
            mensaje = f'Bienvenido {"administrador" if usuario == "juan" else "usuario"} {usuario}'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

    return render_template('ejercicio2.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)

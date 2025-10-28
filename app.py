from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # cambiar para producción

@app.route('/')
def home():
    usuario = session.get('usuario')
    return render_template('home.html', usuario=usuario)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('username')
        clave = request.form.get('password')
        # Validación simulada:
        if usuario == 'alex' and clave == '1234':
            session['usuario'] = usuario
            flash(f'Bienvenido, {usuario}', 'success')
            return redirect(url_for('home'))
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('home'))

@app.route('/register')
def register():
    # Aquí solo simulación: podrías hacer un formulario real luego
    flash('Función de registro (simulada).', 'warning')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

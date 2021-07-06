from flask import Flask,render_template         

#para crear mi objeto
app = Flask(__name__)

#creo una ruta para mi pagina home
@app.route('/')
def home():
    return render_template('home.html')     #con esta ruta retorno la pagina html home

#creo una ruta para mi pagina about
@app.route('/about')
def about():
    return 'funcionando'

if __name__ == '__main__':
    app.run(debug=True)     #debug=true para que los cambios se apliquen sin dejar de correr el cmd


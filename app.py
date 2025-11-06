#SAMARA BREVO MARTINEZ  NL.10    Y  
#  NAOMI BETSABEE ANTUNEZ SANCHEZ NL.4 grupo:306
from flask import Flask, render_template #importa la clase flask y la funcion render_template

app = Flask(__name__)  # crea la aplicación flsk

# --- Datos simulados de películas por género ---
peliculas = {
    'suspenso': [
        {'titulo': 'El silencio de los inocentes', 
        'sinopsis':'Una joven agente del FBI busca la ayuda de un asesino en serie encarcelado para capturar a otro asesino.'},
        {'titulo': 'Perdida',
        'sinopsis': 'Un hombre se convierte en el principal sospechoso cuando su esposa desaparece.'}
    ],
    'terror': [
        {'titulo': 'El exorcista',
        'sinopsis': 'Una niña poseida por una entidad demoniaca.'},
        {'titulo': 'Hereditary',
        'sinopsis': 'Una familia atormentada tras la muerte de su matriarca.'},
    ],
    'romance': [
        {'titulo': 'Orgullo y Prejuicio', 
        'sinopsis': 'Elizabeth Bennet se enfrentaal arrogante Sr. Darcy en la Inglaterra del siglo XIX.'},
        {'titulo': 'LamLa Land', 
        'sinopsis': 'Un pianista de jazz y un aspirante a actriz persiguen sus sueños, en los Angeles.'}
    ],
    'infantil': [
        {'titulo': 'Toy Story',
        'sinopsis': 'Los juguetes cobran vida cuando el dueño no esta.'},
        {'titulo': 'Mi vecino Totoro', 
        'sinopsis': 'Dos hermanas se mudan al campo y descubren al espirito del bosque y se hacen amigas.'},
   ]
}

#--- Ruta principal ---
@app.route('/') # Define la ruta raiz (http://localhost:5000/)
def index():
    return render_template('index.html')  #renderiza la plantilla templates

# --- Ruta dinámica por género ---
@app.route('/suspenso') # Define la ruta /suspenso
def suspenso():
    # pasa lista de peliculas de la categoria suspenso a la plantilla suspenso.html
        return render_template('suspenso.html', peliculas=peliculas['suspenso'])

@app.route('/terror') # Define la ruta /terror
def terror():
    # pasa lista de peliculas de la categoria terror
        return render_template('terror.html', peliculas=peliculas['terror'])

@app.route('/romance') # Define la ruta dinamica /romance
def romance():
    # pasa lista de peliculas de la categoria suspenso a la plantilla suspenso.html
        return render_template('romance.html', peliculas=peliculas['romance'])

@app.route('/infantil') # Define la ruta dinamica /infantil
def infantil():
    # pasa lista de peliculas de la categoria suspenso a la plantilla suspenso.html
        return render_template('infantil.html', peliculas=peliculas['infantil'])


if __name__ == '__main__': # Comprueba si se ejecuta este archivo directamente (no importado)
    app.run(debug=True) # inicia el servidor de desrrollo con recarga automatica y modo debug activado
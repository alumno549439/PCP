from os import getenv
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from forms import MusicaForm  

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

# Conexión a Mongo
cliente = MongoClient(getenv('MONGO_URI'))
db = cliente['coleccion_musica']
tabla = db['discos']

# --- CONSULTAR ---
@app.route('/', methods=['GET'])
def inicio():
    discos = list(tabla.find({}))
    return render_template("inicio.html", discos=discos)

# --- AGREGAR ---
@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    form = MusicaForm()
    if form.validate_on_submit(): 
        nuevo_disco = {
            "artista": form.artista.data,
            "album": form.album.data,
            "genero": form.genero.data
        }
        tabla.insert_one(nuevo_disco)
        return redirect(url_for('inicio'))
    
    return render_template("formulario.html", form=form, accion="Agregar")

# --- ELIMINAR ---
@app.route('/eliminar/<id>')
def eliminar(id):
    tabla.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('inicio'))

# --- EDITAR ---
@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    disco = tabla.find_one({"_id": ObjectId(id)})
    form = MusicaForm(data=disco) 
    
    if form.validate_on_submit():
        tabla.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "artista": form.artista.data,
                "album": form.album.data,
                "genero": form.genero.data
            }}
        )
        return redirect(url_for('inicio'))
        
    return render_template("formulario.html", form=form, accion="Editar")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
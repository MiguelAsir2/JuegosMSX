from flask import Flask,render_template,abort,request
app= Flask(__name__)

import json
with open("MSX.json") as fichero:
    datos=json.load(fichero)


@app.route('/',methods=["GET"])
def inicio():
    return render_template("inicio.html")

@app.route('/juegos',methods=["GET"])
def juegos():
    return render_template("buscajuegos.html")

@app.route('/listajuegos',methods=["POST"])
def listajuegos():
    nombre=request.form["cadena"]
    lista_juegos=[]
    for dato in datos:
        if nombre in str(dato["nombre"]):
            lista_juegos.append(dato)
    return render_template("listajuegos.html",datos=lista_juegos,nombre=nombre)

@app.route('/juego/<id>')
def juego(id):
    juego=[]
    for dato in datos:
        if id == str(dato["id"]):
            juego.append(dato)
            return render_template("juego.html",datos=juego)
        else:
            return abort(404)
        

app.run(debug=True)
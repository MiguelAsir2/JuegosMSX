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
    return render_template("juegos.html")

@app.route('/listajuegos',methods=["POST"])
def listajuegos():
    nombre=request.form["cadena"]
    longitud=len(datos)
    return render_template("listajuegos.html",datos=datos,nombre=nombre,contar=longitud)


app.run(debug=True)
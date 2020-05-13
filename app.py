from flask import Flask,render_template,abort,request
app= Flask(__name__)

import json
import os
with open("MSX.json") as fichero:
    datos=json.load(fichero)


@app.route('/',methods=["GET"])
def inicio():
    return render_template("inicio.html")

#Mejora 1: Búsqueda en una ruta
@app.route('/juegos',methods=["GET","POST"])
def juegos():
    if request.method=="GET":
        categoria=[]
        for dato in datos:
            if dato["categoria"] not in categoria:
                categoria.append(dato["categoria"])
        return render_template("buscajuegos.html",categoria=categoria)
    else:
        nombre=request.form["cadena"]
        lista_juegos=[]
        todos_juegos=[]
        categoria=[]
        for dato in datos:
            todos_juegos.append(dato)
            #Mejora 3: Añadir la busqueda por Categoria.
            if nombre in str(dato["nombre"]) and dato["categoria"] not in categoria :
                lista_juegos.append(dato)
                categoria.append(dato["categoria"])
        return render_template("buscajuegos.html",datos=lista_juegos,nombre=nombre,todo=todos_juegos,categoria=categoria)

@app.route('/juego/<id>')
def juego(id):
    juego=[]
    for dato in datos:
        if id == str(dato["id"]):
            juego.append(dato)
    return render_template("juego.html",datos=juego)

port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=False)
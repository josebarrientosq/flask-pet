"""
APi
"""
from cerberus import Validator
from flask import request, jsonify
from flaskpet import app, db
from flaskpet.models import Persona , Mascota


@app.route('/v1/personas/<nombre>/mascotas', methods=['GET'])
def nombrar_mascotas(nombre):
    """Nombrar las mascotas de una persona

    ---
    tags:
        -   Persona
    parameters:
      - name: nombre
        in: path
        type: string
        required: true
        description: Nombre de la persona

    responses:
        200:
            description: Lista de las mascotas
            schema:
                type : object
                properties:
                    nombre:
                        type : string
        404:
            description : No existe la persona

    """
    persona = Persona.query.filter_by(nombre=nombre).first()

    if persona:
        print(persona.nombre)
        lista = [{"nombre" : nombre} for nombre in persona.nombrar_mascotas()]
        return jsonify(lista),200
    return {"mensaje" : "No existe la persona"},404

@app.route('/v1/personas', methods=['POST'])
def crear_persona():
    """Crear persona dado su nombre
    ejem
    ---
    tags:
        -   Persona
    parameters:
      - name: Persona
        in: body
        required: true
        description: Datos de la persona
        schema:
            type : object
            properties:
                nombre:
                    type : string
                    description: Nombre
            example:
                nombre: swager
    responses:
        201:
            description: Se creo la Persona
        404:
            description: datos invalidos
    """
    schema = {'nombre': {'type': 'string'}}
    validador = Validator(schema)
    params = request.get_json()
    if validador.validate(params):
        nombre = params.get('nombre')
        persona= Persona(nombre)
        db.session.add(persona)
        db.session.commit()
        return {"mensaje" : "Se creo la persona"},201
    return {"mensaje" : "datos invalidos"},404

@app.route('/v1/personas/mascotas', methods=['PUT'])
def obtener_mascota():
    """Obtener una mascota
    Se le asigna a una persona una mascota
    ---
    tags:
        -   Persona
    parameters:
      - in: body
        required: true
        description: Nombre de la persona y mascota
        schema:
            type : object
            properties:
                nombre_persona:
                    type : string
                nombre_mascota:
                    type : string
            example:
                nombre_persona: pepe
                nombre_mascota : doky
    responses:
        200:
            description: se agrego la mascota
        404:
            description: no se encontro la persona o mascota
    """
    params = request.get_json()
    nombre_persona = params.get('nombre_persona')
    nombre_mascota = params.get('nombre_mascota')
    persona = Persona.query.filter_by(nombre=nombre_persona).first()
    mascota = Mascota.query.filter_by(nombre=nombre_mascota).first()
    if persona and mascota:
        persona.obtener_mascota(mascota)
        print(persona.mascotas[0].nombre)
        print(mascota.persona_id.nombre)
        db.session.commit()
        return {"mensaje" : "agrego mascota"},200
    else:
        return {"mensaje" : "no se encontro la persona o mascota"}, 404

@app.route('/v1/personas/<nombre>', methods=['DELETE'])
def borrar_persona(nombre):
    """Borrar persona
    Borrar persona dado su nombre
    ---
    tags:
        -   Persona
    parameters:
      - name: nombre
        in: path
        type: string
        required: true
        description: Nombre de la persona
    responses:
        200:
            description: se elimino la persona
        404:
            description: no se encontro la persona
    """

    persona = Persona.query.filter_by(nombre=nombre).first()
    if persona:
        db.session.delete(persona)
        db.session.commit()
        return {"mensaje" : "se elimino la persona"},200
    return {"mensaje" : "no se encontro la persona"}, 404


@app.route('/v1/mascotas', methods=['POST'])
def crear_mascota():
    """Crear mascota

    ---
    tags:
        -   Mascota
    parameters:
      - name: Persona
        in: body
        required: true
        description: Datos de la persona
        schema:
            type : object
            properties:
                nombre:
                    type : string
                comida_gusta:
                    type : string
            example:
                nombre: doky
                comida_gusta : pollo
    responses:
        201:
            description: Se creo la mascota
            schema:
                type : object
                properties:
                    mensaje:
                        type : string
        404:
            description: Datos invalidos

    """
    schema = {'nombre': {'type': 'string'},'comida_gusta': {'type': 'string'}}
    valid = Validator(schema)
    params = request.get_json()
    if valid.validate(params):
        nombre = params.get('nombre')
        comida = params.get('comida_gusta')
        mascota = Mascota(nombre, comida)
        db.session.add(mascota)
        db.session.commit()
        return {"mensaje" : "se creo la mascota"},201
    return {"mensaje" : "datos invalidos"},404

@app.route('/v1/mascotas', methods=['GET'])
def listar_mascotas():
    """Listar todas las mascotas

    ---
    tags:
        -   Mascota
    responses:
        200:
            description: Lista de las mascotas
            schema:
                type : object
                properties:
                    nombre:
                        type : string
                    comida_gusta:
                        type : string

    """
    mascotas = Mascota.query.all()
    lista=[]
    for mascota in mascotas:
        lista.append({"nombre" : mascota.nombre,
                       "comida" : mascota.comida_gusta })

    return jsonify(lista)

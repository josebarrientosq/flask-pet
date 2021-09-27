"""
El servidor está pensado para satisfacer servicios relacionados a una veterinaria
, se desea desarrollar un entretenido juego para sus clientes sobre gestión de mascotas
enseñarle información sobre animales
"""

from flaskpet import db

class Persona(db.Model):
    """
    Una persona tiene un nombre  varias mascotas  y preparar comida
    """
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(length=30), nullable=False,unique=True)
    mascotas = db.relationship('Mascota', backref='mascota.Persona', lazy=True) #one to many
    comida = db.relationship('Comida', backref='comida.Persona',uselist=False, lazy=True) #onetoone

    def __init__(self,nombre):
        """
        """
        self.nombre = nombre
        self.mascotas = []

    def obtener_mascota(self, mascota):
        """
        Obtener una nueva mascota
        """
        self.mascotas.append(mascota)
        mascota.persona_id = self

    def nombrar_mascotas(self):
        """
        nombrar todas sus mascotas
        """
        nombres=[]
        for mascota in self.mascotas:
            nombres.append(mascota.nombre)
        return nombres

    def preparar_comida(self,comida):
        """
        preparar comida
        """
        self.comida = comida
        comida.persona_id = self

    def dar_comer(self,mascota):
        """
        dar de comer
        """
        if mascota.comida_gusta == self.comida.nombre:
            return True
        return False

    def revisar_comida(self,dias):
        """
        si vence podrir comida
        """
        if self.comida.vence <= dias:
            self.comida.podrirse()

    def revisar_mascotas(self):
        """
        si la salud es menor igual a cero , la mascota muere
        """
        lista = []
        for mascota in self.mascotas:
            if mascota.salud<=0:
                mascota.morir()
                lista.append(mascota)

        for mascota in lista:
            self.mascotas.remove(mascota)
        return lista

    def presentarse(self):
        """
        nombre y mascotas que tiene
        """
        return f"Hola, soy {self.nombre} y mis mascotas son {self.nombrar_mascotas()}"

class Mascota(db.Model):
    """
    Clase mascota tiene un nombre, un dueño, salud, sueño, comida que le gusta
    """
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(length=30), nullable=False)
    persona_id = db.Column(db.Integer(), db.ForeignKey('persona.id'))
    salud = db.Column(db.Integer(), nullable=False)
    sueño = db.Column(db.Integer(), nullable=False)
    comida_gusta= db.Column(db.String(length=30), nullable=False)
    tipo= db.Column(db.String(length=30), nullable=False)
    esta_vivo = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self, nombre,comida=None, salud=100,sueño=100, tipo="grande", vivo=True):
        """
        """
        self.nombre = nombre
        self.persona_id = None
        self.salud = salud
        self.sueño = sueño
        self.comida_gusta = comida
        self.tipo=tipo
        self.esta_vivo= vivo

    def comer_comida(self,comida):
        """
        si es saludable la comida aumenta en 70 la salud sino bajar 40
        """
        if(comida.saludable):
            self.salud += 70
        else:
            self.salud -= 40

    def saludar(self):
        """
        Decir su dueo y que le gusta comer
        """
        return f"Hola {self.persona_id.nombre} me gusta comer {self.comida_gusta}"

    def jugar(self, mascota):
        """
        Solo juega con su propio tipo de perro
        """
        if self.tipo == mascota.tipo:
            return True
        return False

    def dormir(self):
        """
        aumenta el sueño en 50
        """
        self.sueño += 50

    def morir(self):
        """
        no esta vivo
        """
        self.esta_vivo=False


class Comida(db.Model):
    """
    La comida tiene un nombre y lo prepara una persona , ademas puede podrirse
    """
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(length=30), nullable=False)
    persona_id = db.Column(db.Integer(), db.ForeignKey('persona.id'))
    vence = db.Column(db.Integer(), nullable=False)
    saludable = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self, nombre,saludable=True,vence=None, persona_preparo=None):
        """
        """
        self.nombre = nombre
        self.saludable=saludable
        self.vence=vence
        self.persona_id = persona_preparo

    def podrirse(self):
        """
        no es saludable
        """
        self.saludable=False

    def informacion(self):
        """
        quien lo prepara y quien lo puede comer
        """
        mascotas = []
        for mascota in self.persona_id.mascotas:
            if mascota.comida_gusta == self.nombre:
                mascotas.append(mascota.nombre)
        return f"Lo preparo {self.persona_id.nombre} y lo pueden comer {mascotas}"

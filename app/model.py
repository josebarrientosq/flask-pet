class Persona():
    def __init__(self,nombre):
        self.nombre = nombre
        self.mascotas = []
        self.comida = None

    def obtener_mascota(self, mascota):
        self.mascotas.append(mascota)
        mascota.dueño = self

    def nombrar_mascotas(self):
        nombres=[]
        for mascota in self.mascotas:
            nombres.append(mascota.nombre)
        return nombres

    def preparar_comida(self,comida):
        self.comida = comida
        comida.persona_preparo = self
    
    def dar_comer(self,mascota):
        if mascota.comida_gusta == self.comida.nombre:
            return True
        else:
            return False 

    def revisar_comida(self,dias):
        if self.comida.vence <= dias:
            self.comida.podrirse()

    def revisar_mascotas(self):
        lista = []
        for mascota in self.mascotas:
            if mascota.salud<=0:
                mascota.morir()
                lista.append(mascota)

        for m in lista:
            self.mascotas.remove(m)
        return lista

    def presentarse(self):
        return f"Hola, soy {self.nombre} y mis mascotas son {self.nombrar_mascotas()}"

class Mascota():
    def __init__(self, nombre,comida=None, salud=100,sueño=100, tipo=None, vivo=True):
        self.nombre = nombre
        self.dueño = None
        self.salud = salud
        self.sueño = sueño
        self.comida_gusta = comida
        self.tipo=tipo
        self.esta_vivo= vivo
    
    def comer_comida(self,comida):
        if(comida.saludable):
            self.salud += 70
        else:
            self.salud -= 40
    
    def saludar(self):
        persona = self.dueño
        return f"Hola {persona.nombre} me gusta comer {self.comida_gusta}"

    def jugar(self, mascota):
        if self.tipo == mascota.tipo:
            return True
        else:
            return False
        
    def dormir(self):
        self.sueño += 50
    
    def morir(self):
        self.esta_vivo=False


class Comida():
    def __init__(self, nombre,saludable=True,vence=None, persona_preparo=None):
        self.nombre = nombre
        self.saludable=saludable
        self.vence=vence
        self.persona_preparo = persona_preparo	
    
    def podrirse(self):
        self.saludable=False
    
    def informacion(self):
        mascotas = []
        for mascota in self.persona_preparo.mascotas:
            if mascota.comida_gusta == self.nombre:
                mascotas.append(mascota.nombre)
        return f"Lo preparo {self.persona_preparo.nombre} y lo pueden comer {mascotas}"

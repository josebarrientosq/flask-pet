"""
Test
"""
import unittest
import requests
from flaskpet.models import Persona, Mascota, Comida


class PersonaTests(unittest.TestCase):
    """
    Test para la clase persona
    """
    def test_nombrar_mascotas(self):
        """
        Nombrar a todas tus mascotas
        """
        persona = Persona("jose")
        pet1 = Mascota("boby")
        pet2 = Mascota("rex")
        persona.obtener_mascota(pet1)
        persona.obtener_mascota(pet2)

        self.assertEqual(persona.nombrar_mascotas(),["boby","rex"])

    def test_obtener_mascota(self):
        """
        Obtener una nueva mascota
        """
        persona = Persona("jose")
        pet1 = Mascota("boby")
        persona.obtener_mascota(pet1)
        self.assertEqual(persona.nombrar_mascotas(), ["boby"])

    def test_preparar_comida(self):
        """
        Preparar comida por una persona
        """
        persona = Persona("jose")
        comida = Comida("pollo")
        persona.preparar_comida(comida)
        self.assertEqual(persona.comida, comida)

    def test_dar_comer(self):
        """
        Dar de comer a la mascota y solo aceptara si le gusta
        """
        persona = Persona("jose")
        mascota = Mascota("boby","pollo")
        comida = Comida("pollo")
        #comida = Comida("galleta")
        persona.preparar_comida(comida)
        self.assertTrue(persona.dar_comer(mascota))

    def test_revisar_comida(self):
        """
        Revisar si la comida se ha podrido (verificar fecha de caducidad
        y podrir la comida si se paso)
        """
        persona = Persona("jose")
        comida = Comida("pollo",vence=3)
        persona.preparar_comida(comida)
        persona.revisar_comida(dias=2)
        self.assertTrue(persona.comida.saludable)

    def test_revisar_mascotas(self):
        """
        Revisar mascotas (Si la mascota tiene salud <=0 debe morir)
        """
        persona = Persona("jose")
        pet1 = Mascota("boby", salud=100)
        pet2 = Mascota("rex", salud=0)
        pet3 = Mascota("max", salud=-30)
        persona.obtener_mascota(pet1)
        persona.obtener_mascota(pet2)
        persona.obtener_mascota(pet3)
        persona.revisar_mascotas()
        self.assertEqual(persona.nombrar_mascotas(), ["boby"])

    def test_presentarse(self):
        """
        Presentarse (Mostrar su información)
        """
        persona = Persona("jose")
        pet1 = Mascota("boby")
        pet2 = Mascota("rex")
        persona.obtener_mascota(pet1)
        persona.obtener_mascota(pet2)
        self.assertEqual(persona.presentarse(), f"Hola, soy {persona.nombre} y \
        mis mascotas son {persona.nombrar_mascotas()}")

    if __name__ == "__main__":
        unittest.main()

class MascotaTests(unittest.TestCase):
    """
    Test para la clase mascota
    """
    def test_comer_comida(self):
        """
        Comer comida (Si come comida podrida,
        se le restara 40 de salud, sino aumentar 70 de salud)
        """
        mascota = Mascota("boby", "pollo", 100, 100)
        comida1 = Comida("pollo",saludable=True)
        mascota.comer_comida(comida1)
        self.assertEqual(mascota.salud,170)
        comida2 = Comida("pollo",saludable=False)
        mascota.comer_comida(comida2)
        self.assertEqual(mascota.salud, 130)

    def test_saludar(self):
        """
        Saludar a la persona que lo cuida diciendo su comida favorita
        """
        persona = Persona("jose")
        mascota = Mascota("boby", "pollo")
        persona.obtener_mascota(mascota)
        self.assertEqual(mascota.saludar(), f"Hola {mascota.persona_id.nombre} \
        me gusta comer {mascota.comida_gusta}")

    def test_jugar(self):
        """
        Jugar con otra mascota (Las mascotas solo juegan con otras mascotas del mismo tipo)
        """
        mascota1 = Mascota("boby",tipo="grande")
        mascota2 = Mascota("rex", tipo="grande")
        mascota3 = Mascota("canela", tipo="pequeño")

        self.assertTrue(mascota1.jugar(mascota2) )
        self.assertFalse(mascota1.jugar(mascota3))

    def test_dormir(self):
        """
        Dormir (Aumenta su estado de sueño)
        """
        mascota = Mascota("boby", sueño=50)
        mascota.dormir()
        self.assertEqual(mascota.sueño, 100)

    def test_morir(self):
        """
        morir
        """
        mascota = Mascota("boby")
        mascota.morir()
        self.assertFalse(mascota.esta_vivo)


class ComidaTests(unittest.TestCase):
    """
    Test para la clase comida
    """

    def test_podrirse(self):
        """
        Podrir comida
        """
        comida = Comida("pollo")
        comida.podrirse()
        self.assertFalse(comida.saludable)

    def test_informacion_comida(self):
        """
        Información (Describe quien lo preparó, y que mascotas pueden alimentarse de esta)
        """
        persona = Persona("jose")
        pet1 = Mascota("boby", comida="pollo")
        pet2 = Mascota("rex", comida="atun")
        pet3 = Mascota("max", comida="pollo")
        persona.obtener_mascota(pet1)
        persona.obtener_mascota(pet2)
        persona.obtener_mascota(pet3)

        comida = Comida("pollo")
        persona.preparar_comida(comida)

        self.assertEqual(comida.informacion(), f"Lo preparo {comida.persona_id.nombre}\
             y lo pueden comer {['boby','max']}")

class apiTests(unittest.TestCase):
    def test_nombrar_mascotas_api(self):
        nombre="jose"

        url = f"http://127.0.0.1:5000/v1/personas/<{nombre}>/mascotas"
        response = requests.get(url)
        self.assertEqual(response.status_code , 200)

    def test_hola_api(self):
        url = "http://127.0.0.1:5000/"
        response = requests.get(url)
        self.assertEqual(response.status_code , 200)
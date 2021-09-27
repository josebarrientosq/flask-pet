from behave import given , when , then
import requests

@given('Dado el nombre de la persona')
def testConsultaNombre(context):
    nombre = "pepe"
    context.url = f"http://127.0.0.1:5000/v1/personas/<{nombre}>/mascotas"

@when('Cuando envio los datos al api /personas/{nombre}/mascotas')
def consulta(context):
    context.res = requests.get(context.url)

@then('obtengo las mascotas de la persona')
def respuesta(context):
    assert context.res.status_code == 200
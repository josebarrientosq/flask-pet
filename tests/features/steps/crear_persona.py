from behave import given , when , then
import requests

@given('Con el nombre de la persona')
def testConsultaNombre(context):
    context.nombre = "behave"
    context.url = "http://127.0.0.1:5000/v1/personas/"

@when('Cuando envio los datos al api /personas')
def consulta(context):
    data={"nombre": context.nombre}
    context.res = requests.post(context.url,data)

@then('Entonces se crea una persona')
def respuesta(context):
    print(context.res.status_code)
    assert context.res.status_code == 201
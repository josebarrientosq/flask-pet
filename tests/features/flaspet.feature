Feature: flaspet
  
  Scenario: Crear una persona 
     Given Con el nombre de la persona
     When Cuando envio los datos al api /personas
     Then Entonces se crea una persona

  Scenario: Obtener las mascotas de la persona
     Given Dado el nombre de la persona
     When Cuando envio los datos al api
     Then obtengo las mascotas de la persona
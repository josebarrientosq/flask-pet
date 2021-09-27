# Flaskpet
Es una microservicio para la gestion de mascotas, las personas y la comida
###	Métodos para Persona:
1. Nombrar los nombre de todas sus mascotas 
2. Dar comida a una mascota (La mascota solo aceptará la comida que le gusta, no se acepta comida) 
3. Preparar comida 
4, Obtener una nueva mascota 
5. Revisar si la comida se ha podrido (verificar fecha de caducidad y podrir la comida si se paso)
6. Comer (Aumenta su salud) 
7. Dormir (Aumenta su estado de sueño) 
8. Revisar mascotas (Si la mascota tiene salud <=0 debe morir)
9. Presentarse (Mostrar su información) 
### Métodos para Mascotas
1. Comer comida (Si come comida podrida, se le restara 40 de salud, sino aumentar 70 de salud) 
2. Saludar a la persona que lo cuida diciendo su comida favorita 
3. Comunicarse (Se puede usar un print) 
4. Jugar con otra mascota (Las mascotas solo juegan con otras mascotas del mismo tipo)
5. Dormir (Aumenta su estado de sueño) 
6. Morir  
###	Métodos para la comida
1. Podrirse (La comida se pudre)
2. Información (Describe quien lo preparó, y que mascotas pueden alimentarse de esta)


## Create a virtual enviroment
```
python3 -m venv ~/.flask-pet
source ~/.flask-pet/bin/activate
which python3
```

## ejecutar Makefile 
```
make init
make lint
make test
make behave
make run
``` 

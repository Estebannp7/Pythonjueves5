diccionario ={
    'nombre':'Esteban',
    'equipo': 'nacional',
    'edad':21,
    'estatura':'1.68',
    'RH':'A+',
    'Ciudad':'Medellin'
}

#Accediendo de forma individual a los atributos y valores de un dicionario
#print(diccionario)
#print(diccionario['nombre'])
#print(diccionario.get('edad'))


#Acceder a TODOS los atributos y valores 
#De un diccionario al mismo tiempo
#RECORRER UN DICCIONARIO
for clave in diccionario.items():
    print(clave)


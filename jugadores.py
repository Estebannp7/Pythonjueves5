

opcion = 100

print("***Empanadas inteligentes***")
print("1. Agregar Clientes")
print("2.Mostar")
print("0. Salir")


#LISTA
clientes=[]



while(opcion !=0):

    #DICCIONARIO
    cliente={}
    #Pedimos la opcion deseada
    opcion= int(input("Digite la opcion deseada: "))
    #Caminos del menu
    if(opcion==1):
        cliente['cedula'] = input("digite su cedula: ")
        cliente['nombre']= input("Digite  su nombre: ")
        clientes.append(cliente)
        
    elif(opcion==0):
        break
    elif(opcion==2):
        print(cliente)
    elif(opcion==3):
        cedulaABuscar = input("digite la cedula: ")
        for cliente in clientes:
            if(cliente["cedula"]==cedulaABuscar):
                print(f"cliente encontrado:{cliente['cedula']}")
            else:
                print ("Usuario no encontrado")       
    else:
        print("Digite una opcion valida")   

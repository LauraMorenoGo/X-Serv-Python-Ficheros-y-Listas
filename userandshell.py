#!/usr/bin/python3

myfile = open('/etc/passwd', 'r')

dictionary = {}                 #creamos un diccionario vacío
for file in myfile:
    list = file.split(':')      #dividimos lo que está delante y detrás de :
    user = list[0]              #nos quedamos con el primer elemento 
    shell = list[-1]            #nos quedamos con el último elemento
    print("User:", user, "   Shell:", shell)
    
    dictionary[user] = shell    #guardamos cada user y shell en el diccionario creado al principio

print("Parte opcional 1:\n")
print(dictionary)

print("\nParte opcional 2:\n")
print("Shell de root:", dictionary['root'])     #buscamos la entrada root e imprimimos su contenido 
print("Shell de imaginario:", dictionary['imaginario'])

myfile.close()

   
    

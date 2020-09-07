"""
Created on Tue Aug 25 14:03:03 2020

@author: Carlos Bermudez
"""
#Se importan las listas que contienen los datos para nuestro análisis
from lifestore_file import lifestore_products 
from lifestore_file import lifestore_searches
from lifestore_file import lifestore_sales

"""
Para empezar se recomienda iniciar sesión con alguno de los usuarios en lista admin_system,
así podrá regristrar su usuario, dando la opción 1, luego pedirá datos como: nombre, apellido,
contraseña y si está autorizado o no, con un usuario autorizado podrá acceder al contenido de ventas. 
"""
admin_system = [["Carlos Bermudez", "Passw0rd25"],
                ["Sandra Palma", "Passw0rd20"]]
#Si el usuario se equivoca mas de 3 veces con su contraseña se eliminará el ususario
intentos = 0
while intentos <= 3 :
    usuario = input("Usuario: ")
    password = input("Contraseña: ")
    for admin in admin_system:
        if usuario == admin[0] and password == admin[1]:
            autorizacion = "maybe"
            intentos = 4
            #Se despliega las opciones que se pueden hacer como admin_system
            print ("\nHola", usuario.split()[0], ", es un gusto verte de nuevo.\n"
                   "Si deseas agregar un usuario escribe [1].\n"
                   "Si deseas eliminar un usuario escribe [2].\n"
                   "Si deseas ver los usuarios escribe [3].\n"
                   "Si deseas salir escribe [4]\n"
                   "Recuerda que sólo debes de escribir el número dentro de [].")
            respuesta = input("Opción: ")
            count = 0
            while count < 1:
                """
                Con la opción 1 se pueden agregar los usuarion que deseen, la opcion 2 sirve para eliminar usuarios,
                la opcion 3 imprime los usuarios que están registrados, y la 4 es para salir del sistema.
                Se usan archivos de texto para guardar los datos, se usan las funciones de open(), close(), readlines(),
                write() para la manipulación de los archivos de texto
                """
                if "1" in respuesta:
                    rectificacion = input("¿Desea agregar un usuario? Sí[1]/ No[0]: ")
                    if "1" in rectificacion:
                        repetir = 0
                        while repetir < 1:
                            archivo = open("usuarios.txt", "a")
                            nombre = input("Nombre: ")
                            apellido = input("Apellido: ")
                            contraseña = input("Contraseña: ")
                            acceso = input("¿Tiene acceso a la información? Sí[1]/ No[0]: ")
                            if acceso == "1":
                                acceso = "autorizado"
                            else:
                                acceso = "no autorizado"
                            #Con ayuda de format() le damos orden para guardar de mejor manera los datos
                            archivo.write("\n{} {},{},{}".format(nombre, apellido, contraseña, acceso))
                            archivo.close()
                            repetir_accion = input("¿Desea agregar a alguien más? Sí[1]/ No[0]: ")
                            if repetir_accion != "1":
                                repetir = 1
                                nueva_accion = input ("Requiere hacer otra acción. Sí[1]/ No[0]:  ")
                                if nueva_accion == "1":
                                    respuesta = input("Volver a elegir opción: ")
                                else:
                                    print("Hasta la vista Baby")
                                    count = 1
                    else:
                        respuesta = input("Volver a elegir opción: ")
                elif "2" in respuesta:
                    rectificacion = input("¿Desea eliminar un usuario? Sí[1]/ No[0]: ")
                    if "1" in rectificacion:
                        repetir = 0
                        while repetir < 1:
                            usuario_eliminado = input("Usuario a eliminar: ")
                            archivo = open("usuarios.txt", "r")
                            lines = archivo.readlines()
                            archivo.close()
                            nuevo_archivo = open("usuarios.txt", "w")
                            for line in lines:
                                if not usuario_eliminado in line:
                                    nuevo_archivo.write(line)
                            nuevo_archivo.close()        
                            repetir_accion = input("¿Desea eliminar a alguien más? Sí[1]/ No[0]: ")
                            if repetir_accion != "1":
                                repetir = 1
                                nueva_accion = input ("Requiere hacer otra acción. Sí[1]/ No[0]:  ")                                
                                if nueva_accion == "1":
                                    respuesta = input("Volver a elegir opción: ")
                                else:
                                    print("MAY THE FORCE BE WITH YOU")
                                    count = 1
                    else:
                        respuesta = input("Volver a elegir opción: ")
                elif "3" in respuesta:
                    rectificacion = input("¿Desea ver los usuarios? Sí[1]/ No[0]: ")
                    if "1" in rectificacion:
                        files = open("usuarios.txt", "r")
                        for linea in files:
                            lista = linea.strip().split(",")
                            print(lista[0])
                        files.close()
                        nueva_accion = input ("Requiere hacer otra acción. Sí[1]/ No[0]:  ")                                
                        if nueva_accion == "1":
                            respuesta = input("Volver a elegir opción: ")
                        else:
                            print("Hasta el infinito y mas allá")
                            count = 1
                    else:
                        respuesta = input("Volver a elegir opción: ")
                elif "4" in respuesta:
                    print()
                    rectificacion = input("¿Desea salir? Sí[1]/ No[0]: ")
                    if "1" in rectificacion:
                        print("No me quiero ir señor Stark")
                        break
                    else:
                        respuesta = input("Volver a elegir opción: ")
        #Los administradores no tienen limite de fallos en la contraseña
        elif usuario == admin[0] and password != admin[1]:
            print("Contraseña incorrecta intente de nuevo.")
    #En esta parte se analiza la entrada del usuario por si no es un administrador    
    archivo = open("usuarios.txt", "r")
    for linea in archivo.readlines():        
        if usuario in linea:
            #Se usa strip() para quitar los saltos de linea a la hora de recuperar los datos
            #Se usa split() para crear una lista con los datos obtenidos del archivo ususarios.txt
            if usuario == linea.strip().split(",")[0] and password == linea.strip().split(",")[1]:
                intentos = 4
                if linea.strip().split(",")[2] =="autorizado":
                    autorizacion = "sí"
                else:
                    autorizacion = "no"
            elif intentos == 2:
                print("Contraseña incorrecta, último intento.")
                intentos += 1
            elif intentos == 3: #Caundo se llega a3 intentos fallidos se elimina el usuario
                print("Por seguridad su usuario será eliminado")
                archivo = open("usuarios.txt", "r")
                lines = archivo.readlines()
                archivo.close()
                nuevo_archivo = open("usuarios.txt", "w")
                for line in lines:
                    if not usuario in line:
                        nuevo_archivo.write(line)
                nuevo_archivo.close()
                intentos += 1
            else:
                intentos += 1
                print("Contraseña incorrecta intente de nuevo")
    archivo.close()
total_products = len(lifestore_products) #número de productos qeuse venden
#Se crean listas para in contando las busquedas y puntuación.
count_searches = []
count_score = []
for n in range(total_products):
    count_searches.append([n+1,0,lifestore_products[n][1]])
    count_score.append([n+1,0,0,lifestore_products[n][1]])
    for search in lifestore_searches:
        if search[1] == count_searches[n][0]:
            count_searches[n][1] += 1
    for search in lifestore_sales:
         if search[1] == count_score[n][0]:
             count_score[n][1] += search[2]
             count_score[n][2] += 1
#Se seaparan los productos de los que sí tienen busquedas de los que no.
without_searches = []
with_searches = []
with_searches_copy =[]
for count in count_searches:
    if count[1] != 0:
        with_searches.append(count)
        with_searches_copy.append(count)
    else:
        without_searches.append(count)
searches_ordenado_menos = []
searches_ordenado_mas = []
#Se ordenan los valores de menor busqueda a mayor busqueda
while with_searches:
    minimo = with_searches[0][1]
    searches_actual = with_searches[0]
    for search in with_searches:
        if search[1] < minimo:
            minimo = search[1]
            searches_actual = search
    searches_ordenado_menos.append(searches_actual)
    with_searches.remove(searches_actual)
#Se ordenan los valores de mayor busqueda a menor
while with_searches_copy:
    maximo = with_searches_copy[0][1]
    searches_actual = with_searches_copy[0]
    for search in with_searches_copy:
        if search[1] > maximo:
            maximo = search[1]
            searches_actual = search
    searches_ordenado_mas.append(searches_actual)
    with_searches_copy.remove(searches_actual)
vendidos = []
vendidos_copy = []
promedio = []
promedio_copy = []
sin_registro = []
for score in count_score:
    if score[2] != 0:
        vendidos.append([score[0],score[2],score[3]])
        vendidos_copy.append([score[0],score[2],score[3]])
        promedio.append([score[0], round(score[1]/score[2],2),score[3]])
        promedio_copy.append([score[0], round(score[1]/score[2],2),score[3]])
    else:
        sin_registro.append([score[0], "Sin registro de venta"])
#Se ordenan productos mas a vendidos, puntuacionde mayor a menor y de menor a mayor
vendidos_mas = []
vendidos_menos = []
promedio_mas = []
promedio_menos = []
while vendidos:
    minimo = vendidos[0][1]
    ventas_actual = vendidos[0]
    for ventas in vendidos:
        if ventas[1] < minimo:
            minimo = ventas[1]
            ventas_actual = ventas
    vendidos_menos.append(ventas_actual)
    vendidos.remove(ventas_actual)
while promedio_copy:
    maximo =promedio_copy[0][1]
    promedio_actual = promedio_copy[0]
    for puntuacion in promedio_copy:
        if puntuacion[1] > maximo:
            maximo = puntuacion[1]
            promedio_actual = puntuacion
    promedio_mas.append(promedio_actual)
    promedio_copy.remove(promedio_actual)
while promedio:
    minimo = promedio[0][1]
    promedio_actual = promedio[0]
    for puntuacion in promedio:
        if puntuacion[1] < minimo:
            minimo = puntuacion[1]
            promedio_actual = puntuacion
    promedio_menos.append(promedio_actual)
    promedio.remove(promedio_actual)
while vendidos_copy:
    maximo = vendidos_copy[0][1]
    vendidos_actual = vendidos_copy[0]
    for ventas in vendidos_copy:
        if ventas[1] > maximo:
            maximo = ventas[1]
            vendidos_actual = ventas
    vendidos_mas.append(vendidos_actual)
    vendidos_copy.remove(vendidos_actual)
#Se crean listas para el calculo de ventas por mes y anual, tambien se ordenan de mayor a menor
by_date = []
for sale in lifestore_sales:
    by_date.append([lifestore_products[sale[1]-1][2],sale[3][3:],sale[4]])
month_list = []
year_list= []
for month in by_date:
    if not month[1] in month_list:
        month_list.append(month[1])
    if not month[1][-4:] in year_list:
        year_list.append(month[1][-4:])
contador_ventas_mensual = []
for month in month_list:
    contador_ventas_mensual.append([month, 0])
for sale in by_date:
    for month in contador_ventas_mensual:
        if sale[1] == month[0]:
            month[1] += sale[0]
contador_ventas_anual = []
for year in year_list:
    contador_ventas_anual.append([year,0,0])
for sale in contador_ventas_mensual:
    for year in contador_ventas_anual:
        if sale[0][-4:] == year[0]:
            year[1] += sale[1]
            year[2] += 1
meses_mayor_ventas = []
while contador_ventas_mensual:
    maximo = contador_ventas_mensual[0][1]
    vendidos_actual = contador_ventas_mensual[0]
    for ventas in contador_ventas_mensual:
        if ventas[1] > maximo:
            maximo = ventas[1]
            vendidos_actual = ventas
    meses_mayor_ventas.append(vendidos_actual)
    contador_ventas_mensual.remove(vendidos_actual)
meses = ["Enero", "Febrero","Marzo","Abril","Mayo","Junio",
         "Julio", "Agosto","Septiembre","Octubre","Noviembre", "Diciembre"]
"""
Si el usuario está autorizado podrá acceder a datos de productos más vendidos, menos vendidos,
mas buscados, menos buscados, sin buscar, sin ventas, con las mejores reseñas o las peores,
tambien se puede acceder a la venta total anual, o mensuales.
Se puede escoger la cantidad de productos a desplegar, pueden ser 1 hasta los que quiera el usuario,
si el usuario quiere mas de los que hay disponibles, no hay problema el sistema solo desplegara los que hay 
"""
if autorizacion == "sí":
    print("Acceso autorizado")
    print ("Hola", usuario, ", es un gusto verte de nuevo.\n"
    "Si deseas ver top productos más vendidos escribe [1].\n"
    "Si deseas ver top productos menos vendidos escribe [2].\n"
    "Si deseas ver top productos más buscados escribe [3].\n"
    "Si deseas ver top productos menos buscados escribe [4]\n"
    "Si deseas ver top productos sin busquedas [5]\n"
    "Si deseas ver top productos mejores reseñas escribe [6]\n"
    "Si deseas ver top productos peores reseñas escribe [7]\n"
    "Si deseas ver los productos sin ventas escribe [8]\n"
    "Si deseas ver total ventas escribe [9]\n"
    "Recuerda que sólo debes de escribir el número dentro de [].")
    opcion = input("Elegir opción: ")
    continuar = 0
    
    while continuar < 1:
        #Top de mas vendidos
        if "1" in opcion:
            print("Máximo de datos a ver {}".format(str(len(vendidos_mas))))
            top = int(input("Número de datos a ver: "))
            if top > len(vendidos_mas):
                top = len(vendidos_mas)
            print("{} más vendidos:".format(top))
            for n in range(top):
                print("{:>2s}. {:>3s} piezas se vendieron de {}".format(str(n+1),str(vendidos_mas[n][1]),vendidos_mas[n][2].split(",")[0]))
            eleccion = input("¿Desea ver otro dato? Sí[1]/ No[0]: ")
            if eleccion == "1":
                opcion = input("Elegir opción: ")
            else:
                continuar = 1
        #Top de menos vendidos
        elif "2" in opcion:
            print("Máximo de datos a ver {}".format(str(len(vendidos_menos))))
            top = int(input("Número de datos a ver: "))
            if top > len(vendidos_menos):
                top = len(vendidos_menos)
            print("{} menos vendidos:".format(top))
            for n in range(top):
                print("{:>2s}. {:>3s} piezas se vendieron de {}".format(str(n+1),str(vendidos_menos[n][1]),vendidos_menos[n][2].split(",")[0]))
            eleccion = input("¿Desea ver otro dato? Sí[1]/ No[0]: ")
            if eleccion == "1":
                opcion = input("Elegir opción: ")
            else:
                continuar = 1
        #top de mas buscados
        elif "3" in opcion:
            print("Máximo de datos a ver {}".format(str(len(searches_ordenado_mas))))
            top = int(input("Número de datos a ver: "))
            if top > len(searches_ordenado_mas):
                top = len(searches_ordenado_mas)
            print("{} más buscados:".format(top))
            for n in range(top):
                print("{:>2s}. {:>3s} busquedas de {}".format(str(n+1),str(searches_ordenado_mas[n][1]),searches_ordenado_mas[n][2].split(",")[0]))
            eleccion = input("¿Desea ver otro dato? Sí[1]/ No[0]: ")
            if eleccion == "1":
                opcion = input("Elegir opción: ")
            else:
                continuar = 1
        #top de menos buscados
        elif "4" in opcion:
            print("Máximo de datos a ver {}".format(str(len(searches_ordenado_menos))))
            top = int(input("Número de datos a ver: "))
            if top > len(searches_ordenado_menos):
                top = len(searches_ordenado_menos)
            print("{} menos buscados:".format(top))
            for n in range(top):
                print("{:>2s}. {:>3s} busquedas de {}".format(str(n+1),str(searches_ordenado_menos[n][1]),searches_ordenado_menos[n][2].split(",")[0]))
            eleccion = input("¿Desea ver otro dato? Sí[1]/ No[0]: ")
            if eleccion == "1":
                opcion = input("Elegir opción: ")
            else:
                continuar = 1            
        #Lista de productos sin busquedas
        elif "5" in opcion:
            print("Productos sin búsquedas: ")
            indice = 0
            for product in lifestore_products: 
                for busqueda in without_searches:
                    if busqueda[0] == product[0]:
                        indice += 1
                        print("{:>2s}. {}".format(str(indice), product[1].split(",")[0]))
            eleccion = input("¿Desea ver otro dato? Sí[1]/ No[0]: ")
            if eleccion == "1":
                opcion = input("Elegir opción: ")
            else:
                continuar = 1
        #Mejores puntuados
        elif "6" in opcion:
            print("Máximo de datos a ver {}".format(str(len(promedio_mas))))
            top = int(input("Número de datos a ver: "))
            if top > len(promedio_mas):
                top = len(promedio_mas)
            print("{} mejores puntuados:".format(top))
            for n in range(top):
                print("{:>2s}. Calificación {:>2s}/5 de {}".format(str(n+1),str(promedio_mas[n][1]),promedio_mas[n][2].split(",")[0]))
            eleccion = input("¿Desea ver otro dato? Sí[1]/ No[0]: ")
            if eleccion == "1":
                opcion = input("Elegir opción: ")
            else:
                continuar = 1
        #Peores puntuados
        elif "7" in opcion:
            print("Máximo de datos a ver {}".format(str(len(promedio_menos))))
            top = int(input("Número de datos a ver: "))
            if top > len(promedio_menos):
                top = len(promedio_menos)
            print("{} peores puntuados:".format(top))
            for n in range(top):
                print("{:>2s}. Calificación {:>2s}/5  de {}".format(str(n+1),str(promedio_menos[n][1]),promedio_menos[n][2].split(",")[0]))
            eleccion = input("¿Desea ver otro dato? Sí[1]/ No[0]: ")
            if eleccion == "1":
                opcion = input("Elegir opción: ")
            else:
                continuar = 1
        #Lista de productos sin ventas
        elif "8" in opcion:
            print("Productos sin ventas: ")
            indice = 0
            for product in lifestore_products: 
                for registro in sin_registro:
                    if registro[0] == product[0]:
                        indice += 1
                        print("{:>2s}. {}".format(str(indice), product[1].split(",")[0]))
            eleccion = input("¿Desea ver otro dato? Sí[1]/ No[0]: ")
            if eleccion == "1":
                opcion = input("Elegir opción: ")
            else:
                continuar = 1
        #Datos de ventas, anuakles y mensuales
        elif "9" in opcion:
            print("Ventas anuales")
            for year in contador_ventas_anual:
                print("{}: $ {},{}.00".format(year[0],str(year[1])[:-3],str(year[1])[-3:]))
            print("Promedio mensual")
            for year in contador_ventas_anual:
                promedio_mensual = str(round(year[1]/year[2],2))
                print("{}: $ {}".format(year[0],promedio_mensual))
            print("Ventas por mes")
            indice = 0
            for mes in meses_mayor_ventas:
                indice += 1
                a = int(mes[0][:2])-1
                print("{:>2s}. {:>10s} {}: ${},{}.00".format(str(indice),meses[a],mes[0][-4:],str(mes[1])[:-3],str(mes[1])[-3:]))
            eleccion = input("¿Desea ver otro dato? Sí[1]/ No[0]: ")
            if eleccion == "1":
                opcion = input("Elegir opción: ")
            else:
                continuar = 1
elif autorizacion == "maybe": #Esto es para evitar que salga el mensaje de no autorizado al admin_system
    print("")
else:
    print("Acceso no autorizado, adiós. >.<")#si los usuarios no estan autorizados sale este mensaje           


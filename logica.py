import random
NO_ENCONTRADO = False
ENCONTRADO = True
FIN_DE_ORACION = "" 

#pide la ruta de un archivo de chat, lee y separa el contacto y sus mensajes.
def leer_archivo(ruta):
    if not validar_archivo(ruta):
        return
    with open (ruta, "r", encoding= "utf-8") as f:
        dicc_contacto_mensajes = {}
        for linea in f:
            chat = linea.strip().split("- ", 1)
            partes = chat[1].split(": ", 1)
            if len(partes) == 2:
                contacto, oracion = partes
                if contacto not in dicc_contacto_mensajes.keys():
                    dicc_contacto_mensajes[contacto] = [[oracion.lower()]]
                else:
                    dicc_contacto_mensajes[contacto].append([oracion.lower()])
    return dicc_contacto_mensajes

#a partir de una serie de palabras, contar las veces que cada contacto dijo cada palabra
def contar_palabras(serie_palabras, dicc_contacto_mensajes, ruta_destino):
    with open(ruta_destino, "w") as f_destino:
        f_destino.write("contacto,palabra,frecuencia \n")                                                                
        acumulador_palabras = {}         
        for palabra_especifica in serie_palabras:                                                                                                                            
            palabra_especifica = palabra_especifica.lower()
            frecuencia_por_contacto = {} 
            for contacto, mensajes in dicc_contacto_mensajes.items(): 
                acumulador = 0
                for mensaje in mensajes:
                    palabras =  mensaje[0].split()            
                    for palabra in palabras:  
                        if palabra == palabra_especifica:
                            acumulador += 1
                frecuencia_por_contacto[contacto] = acumulador
            acumulador_palabras[palabra_especifica] = frecuencia_por_contacto
        for palabra_especifica in serie_palabras:
            for contacto in dicc_contacto_mensajes:
                palabra_especifica = palabra_especifica.lower()
                frecuencia = acumulador_palabras[palabra_especifica][contacto]
                f_destino.write(f"{contacto},{palabra_especifica},{frecuencia} \n")
    return 
    
#a partir del contacto va a generar un mensaje pseudo-aleatorio
def generar_mensaje(contacto, d_palabra_siguiente, comienzo_oracion):
    palabra = random.choice(comienzo_oracion[contacto])
    oracion = palabra
    while palabra is not FIN_DE_ORACION:
        palabra = random.choice(d_palabra_siguiente[contacto][palabra])
        oracion += " " + palabra
    return oracion



def inicializar_diccionarios(dicc_contacto_mensajes): #chat= list[list0[str1, str2, str3,.....strn]]
    comienzo_oracion = {}
    d_palabra_siguiente = {}
    for contacto, chat in dicc_contacto_mensajes.items():
        dicc_contacto_palabras = {}
        for mensajes in chat:
            for mensaje in mensajes:
                palabras = mensaje.split()
                comienzo_oracion[contacto] = [palabras[0]] 
                for indice, palabra in enumerate(palabras[:-1]):
                    palabra_siguiente = palabras[indice + 1]
                    if palabra not in dicc_contacto_palabras:
                        dicc_contacto_palabras[palabra] = [palabra_siguiente]
                    else:
                        dicc_contacto_palabras[palabra].append(palabra_siguiente)
                if palabras[-1] not in dicc_contacto_palabras:
                    dicc_contacto_palabras[palabras[-1]] = [FIN_DE_ORACION]
                else:
                    dicc_contacto_palabras[palabras[-1]].append(FIN_DE_ORACION)
            d_palabra_siguiente[contacto] = dicc_contacto_palabras
    return d_palabra_siguiente, comienzo_oracion


def validar_archivo(ruta):
    try: archivo = open(ruta)
    except: 
        print(f"Error al abrir el archivo: {ruta}")
        return NO_ENCONTRADO
    archivo.close()
    return ENCONTRADO





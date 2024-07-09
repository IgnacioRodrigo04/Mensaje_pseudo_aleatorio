import logica 
import os
import platform
OPCION_VACIA = ""

def leer_ruta():
    ruta = input("Ingrese una ruta de archivo de chat: ")
    clear_screen()
    dicc_contacto_mensajes = logica.leer_archivo(ruta)
    return dicc_contacto_mensajes

def mostrar_menu():
    while True:
        print("1. Generar Archivo de palabras seleccionadas ")      
        print("2. Generar un mensaje pseudo-aleatorio ")
        print("3. Salir ")
        opcion = input(">> ")
        if opcion.isdigit():
            return int(opcion)
    

def mostrar_contar_palabras(dicc_contacto_mensajes):
    serie_palabras = input("Ingrese la palabra para contar entre contactos: ").split()
    ruta_destino = input("Ingrese el archivo destino para guardar el reporte: ")
    clear_screen()
    logica.contar_palabras(serie_palabras, dicc_contacto_mensajes, ruta_destino)

def mostrar_contactos(dicc_contacto_mensajes):
    lista = []
    for indice, contacto in enumerate(dicc_contacto_mensajes.keys()):
        print(f"{indice}. {contacto}")
        lista.append(contacto)
    return lista

def clear_screen():
    system = platform.system()
    if system == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def main():
    clear_screen()
    dicc_contacto_mensajes = leer_ruta()
    if dicc_contacto_mensajes == None:
        return
    d_palabra_siguiente, comienzo_oracion = logica.inicializar_diccionarios(dicc_contacto_mensajes)
    opcion = OPCION_VACIA
    while not opcion == 3:
        opcion = mostrar_menu()
        if opcion == 1:
            mostrar_contar_palabras(dicc_contacto_mensajes)
        elif opcion == 2:
            lista = mostrar_contactos(dicc_contacto_mensajes)
            contacto = input("Ingrese el contacto para generar el mensaje: ")
            clear_screen()
            if contacto.isdigit() and 0 <= int(contacto) <= len(lista) - 1 :
                oracion = logica.generar_mensaje(lista[int(contacto)], d_palabra_siguiente, comienzo_oracion)
                print (f"{lista[int(contacto)]}: {oracion}")
main()  

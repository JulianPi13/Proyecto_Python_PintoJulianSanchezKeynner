# =========================
# IMPORTACIÓN DE MÓDULOS
# =========================

# Módulo para trabajar con archivos JSON (leer información del archivo data.json)
import json

# Módulo para generar valores aleatorios (aunque aquí no se use directamente)
import random


# =========================
# FUNCIÓN PARA CALCULAR FECHA DE FIN
# =========================

# Función que recibe una fecha de inicio y calcula la fecha de finalización
# sumándole exactamente 10 meses
def calcularFechaFin(fechaInicio):
    """Calcula la fecha de fin sumando exactamente 10 meses a la fecha de inicio"""
    try:
        # Divide la fecha usando el carácter "/"
        partes = fechaInicio.split("/")

        # Convierte cada parte a número entero
        dia = int(partes[0])
        mes = int(partes[1])
        año = int(partes[2])
        
        # Suma 10 meses al mes actual
        mes += 10
        
        # Si el mes pasa de 12, se ajusta el año
        while mes > 12:
            mes -= 12
            año += 1
        
        # Retorna la nueva fecha con formato correcto
        return f"{dia:02d}/{mes:02d}/{año}"

    # Si ocurre algún error con la fecha
    except:
        return "Error en fecha"


# =========================
# CARGA DEL ARCHIVO JSON
# =========================

# Abre el archivo data.json en modo lectura
with open("data.json", "r", encoding="utf-8") as archivo:
    # Guarda la información del JSON en la variable datos
    datos = json.load(archivo)


# =========================
# FUNCIÓN PARA INICIAR SESIÓN COMO CAMPER
# =========================

def iniciarSesionCamper():
    
    # Muestra el encabezado del acceso al camper
    print("--- ACCESO CAMPER ---")

    # Solicita el ID del camper
    id_camper = input("Ingrese su ID de Camper: ")

    # Variable para guardar el camper encontrado
    camper_encontrado = None

    # Recorre la lista de campers en el JSON
    for i in datos["campers"]:
        # Compara el ID ingresado con el ID del camper
        if i["id"] == id_camper:
            camper_encontrado = i
            break

    # Si el camper fue encontrado
    if camper_encontrado:
        # Variable booleana para controlar el menú del camper
        booleanito2 = True

        # Ciclo del menú del camper
        while booleanito2 == True:
            print("----------------------------------------------")
            print(f"💻 Has ingresado como Camper: {camper_encontrado['nombres']} 💻")
            print("1. Ver notas")
            print("2. Ver trainer y ruta asignada")
            print("3. Pruebas y trabajos")
            print("4. Salir del ROL Camper")
            print("----------------------------------------------")

            # Solicita la opción que desea ejecutar el camper
            opcionCam = int(input("¿Qué deseas hacer?: "))

            # =========================
            # OPCIÓN 1: VER NOTAS
            # =========================
            if opcionCam == 1:
                print("--- MIS NOTAS ---")
                print("Prueba Teórica (30%): ", camper_encontrado.get("notaPruebaTeorica", 0))
                print("Prueba Práctica (60%): ", camper_encontrado.get("notaPruebaPractica", 0))
                print("Quiz (10%): ", camper_encontrado.get("notaPruebaQuiz", 0))
                print("Examen Inicial: ", camper_encontrado.get("notaExamenInicial", 0))

            # =========================
            # OPCIÓN 2: VER TRAINER Y RUTA
            # =========================
            elif opcionCam == 2:
                ruta_camper = camper_encontrado.get("ruta")
                for trainer in datos["trainers"]:
                    print("Trainer disponible: ", trainer["nombre"])
                print("Ruta asignada: ", camper_encontrado.get("ruta", "No asignada"))
                

            # =========================
            # OPCIÓN 3: VER PRUEBAS Y TRABAJOS
            # =========================
            elif opcionCam == 3:
                print("--- PRUEBAS Y TRABAJOS ---")
                print("Prueba Teórica habilitada: ", camper_encontrado.get("pruebaTeorica", False))
                print("Prueba Práctica habilitada: ", camper_encontrado.get("pruebaPractica", False))
                print("Quiz habilitado: ", camper_encontrado.get("pruebaQuiz", False))

            # =========================
            # OPCIÓN 4: SALIR DEL ROL CAMPER
            # =========================
            elif opcionCam == 4:
                print("----------------------------------------------")
                print(f"👋 Saliendo del rol CAMPER. ¡Hasta luego {camper_encontrado['nombres']}!")
                booleanito2 = False

            # =========================
            # OPCIÓN INVÁLIDA
            # =========================
            else:
                print("⚠️ Opción inválida ⚠️")

    # Si el ID del camper no existe
    else:
        print("⚠️ ID de Camper no válido ⚠️")

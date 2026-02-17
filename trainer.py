# Se importa el módulo json para leer y escribir archivos JSON
import json

# Se importa el módulo random (aunque en este archivo no se use directamente)
import random

# Función que calcula la fecha de fin sumando 10 meses a una fecha inicial
def calcularFechaFin(fechaInicio):
    # Docstring que explica qué hace la función
    """Calcula la fecha de fin sumando exactamente 10 meses a la fecha de inicio"""
    try:
        # Se divide la fecha usando "/" como separador
        partes = fechaInicio.split("/")

        # Se convierte el día a entero
        dia = int(partes[0])

        # Se convierte el mes a entero
        mes = int(partes[1])

        # Se convierte el año a entero
        año = int(partes[2])
        
        # Se suman 10 meses al mes inicial
        mes += 10
        
        # Mientras el mes sea mayor a 12, se ajusta el año
        while mes > 12:
            # Se resta 12 meses
            mes -= 12
            # Se suma 1 al año
            año += 1
        
        # Se retorna la fecha final en formato DD/MM/AAAA
        return f"{dia:02d}/{mes:02d}/{año}"

    # Si ocurre cualquier error, se captura aquí
    except:
        # Se retorna un mensaje de error
        return "Error en fecha"
    

# Se abre el archivo data.json en modo lectura con codificación UTF-8
with open("data.json", "r", encoding="utf-8") as archivo:
    # Se carga el contenido del JSON en la variable datos
    datos = json.load(archivo)
    

# Función para iniciar sesión como Trainer
def iniciarSesionTrainer ():

    # Se muestra el encabezado del acceso Trainer
    print("--- ACCESO TRAINER ---")

    # Se solicita el ID del trainer
    id_trainer = input("Ingrese su ID de Trainer: ")

    # Variable para guardar el trainer encontrado
    trainer_encontrado = None

    # Se recorre la lista de trainers del JSON
    for i in datos["trainers"]:
        # Si el ID coincide con el ingresado
        if i["id"] == id_trainer:
            # Se guarda el trainer encontrado
            trainer_encontrado = i
            # Se rompe el ciclo
            break

    # Si el trainer fue encontrado
    if trainer_encontrado:
        # Variable de control del menú
        booleanito3 = True

        # Bucle del menú del trainer
        while booleanito3:
            # Se imprime el menú
            print("----------------------------------------------")
            print(f"💼 Has ingresado como Trainer: {trainer_encontrado['nombre']} 💼")
            print("1. Habilitar prueba teórica a un Camper")
            print("2. Habilitar prueba práctica a un Camper")
            print("3. Habilitar Quiz a un Camper")
            print("4. Ver mi horario y especialidad")
            print("5. Ver lista de estudiantes")
            print("6. MODIFICAR NOTAS POR ID")
            print("7. Ver estudiantes en mi misma RUTA")
            print("8. Salir del ROL Trainer")
            print("----------------------------------------------")

            # Se solicita la opción del menú
            opcionTrain = int(input("¿Qué deseas hacer?: "))

            # Opciones para habilitar pruebas
            if opcionTrain in [1, 2, 3]:
                # Se pide el ID del camper
                id_c = input("Ingrese el ID del Camper: ")

                # Variable para almacenar el camper encontrado
                camper_encontrado = None

                # Se recorren los campers
                for c in datos["campers"]:
                    # Si el ID coincide
                    if c["id"] == id_c:
                        # Se guarda el camper
                        camper_encontrado = c
                        break

                # Si el camper existe
                if camper_encontrado:
                    # Habilitar prueba teórica
                    if opcionTrain == 1:
                        camper_encontrado["pruebaTeorica"] = True
                        print("✅ Prueba teórica habilitada")

                    # Habilitar prueba práctica
                    elif opcionTrain == 2:
                        camper_encontrado["pruebaPractica"] = True
                        print("✅ Prueba práctica habilitada")

                    # Habilitar quiz
                    elif opcionTrain == 3:
                        camper_encontrado["pruebaQuiz"] = True
                        print("✅ Quiz habilitado")

                    # Se guardan los cambios en el archivo JSON
                    with open("data.json", "w", encoding="utf-8") as f:
                        json.dump(datos, f, indent=4)

                # Si el camper no existe
                else:
                    print("⚠️ Error: el ID del camper no existe ⚠️")

            # Opción para ver horario y especialidad
            elif opcionTrain == 4:
                print("HORARIO:", trainer_encontrado["horario"])
                print("ESPECIALIDAD:", trainer_encontrado["especialidad"])

            # Opción para ver lista de campers
            elif opcionTrain == 5:
                print("--- LISTA DE CAMPERS ---")
                for c in datos["campers"]:
                    print(f"ID: {c['id']} - Nombre: {c['nombres']} {c['apellidos']}")

            # Opción para modificar notas
            elif opcionTrain == 6:
                # Se solicita el ID del camper
                id_buscar = input("Ingrese el ID del Camper a calificar: ")

                # Variable para guardar el camper
                camper_n = None

                # Se busca el camper
                for c in datos["campers"]:
                    if c["id"] == id_buscar:
                        camper_n = c
                        break

                # Si el camper existe
                if camper_n:
                    print(f"Modificando notas de {camper_n['nombres']}")

                    # Se asignan las nuevas notas
                    camper_n["notaPruebaTeorica"] = int(input("Nota Teórica (30%): "))
                    camper_n["notaPruebaPractica"] = int(input("Nota Práctica (60%): "))
                    camper_n["notaPruebaQuiz"] = int(input("Nota Quiz (10%): "))

                    # Se guardan los cambios en el JSON
                    with open("data.json", "w", encoding="utf-8") as f:
                        json.dump(datos, f, indent=4)

                    print("✅ Notas actualizadas correctamente")

                # Si no se encuentra el camper
                else:
                    print("⚠️ Error: ID de camper no encontrado ⚠️")

            # Opción para ver campers en la misma ruta
            elif opcionTrain == 7:
                print("--- CAMPERS EN MI RUTA ---")
                ruta_trainer = trainer_encontrado.get("ruta")
                for camper in datos["campers"]:
                    print(camper["nombres"], camper["apellidos"] )

            # Opción para salir del rol trainer
            elif opcionTrain == 8:
                print("👋 Saliendo del rol TRAINER...")
                booleanito3 = False

            # Si la opción no es válida
            else:
                print("⚠️ Opción inválida ⚠️")

    # Si el ID del trainer no existe
    else:
        print("⚠️ ID de Trainer incorrecto ⚠️")

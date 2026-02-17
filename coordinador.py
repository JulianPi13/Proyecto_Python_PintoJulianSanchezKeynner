# Se importa el módulo json para manejar archivos JSON
import json

# Se importa el módulo random para elecciones aleatorias
import random


# Función que calcula la fecha de finalización sumando 10 meses
def calcularFechaFin(fechaInicio):
    # Docstring que describe la función
    """Calcula la fecha de fin sumando exactamente 10 meses a la fecha de inicio"""
    try:
        # Se separa la fecha usando "/" como delimitador
        partes = fechaInicio.split("/")

        # Se obtiene el día y se convierte a entero
        dia = int(partes[0])

        # Se obtiene el mes y se convierte a entero
        mes = int(partes[1])

        # Se obtiene el año y se convierte a entero
        año = int(partes[2])
        
        # Se suman 10 meses al mes inicial
        mes += 10
        
        # Mientras el mes sea mayor a 12 se ajusta el año
        while mes > 12:
            # Se restan 12 meses
            mes -= 12
            # Se incrementa el año
            año += 1
        
        # Se retorna la fecha final con formato DD/MM/AAAA
        return f"{dia:02d}/{mes:02d}/{año}"

    # Si ocurre cualquier error
    except:
        # Se retorna un mensaje de error
        return "Error en fecha"
    
    
# Se abre el archivo data.json en modo lectura
with open("data.json", "r", encoding="utf-8") as archivo:
    # Se carga la información del JSON en la variable datos
    datos = json.load(archivo)
    

# Función para iniciar sesión como Coordinador
def iniciarSesionCoordinador ():
    
    # Se muestra el encabezado del acceso coordinador
    print("--- ACCESO COORDINADOR ---")

    # Se solicita el ID del coordinador
    idCoordinador = input("Ingrese su ID de Coordinador: ")

    # Variable para guardar el coordinador encontrado
    coordinadorEncontrado = None

    # Se recorre la lista de coordinadores en el JSON
    for i in datos["coordinador/a"]:
        # Si el ID coincide
        if i["id"] == idCoordinador:
            # Se guarda el coordinador
            coordinadorEncontrado = i
            break

    # Si no se encuentra el coordinador
    if coordinadorEncontrado is None:
        print("⚠️ Error: ID del/la coordinador/a no es válido ⚠️")

    # Si el coordinador existe
    else:
        # Variable para controlar el menú del coordinador
        booleanito4 = True
        indiceCamper = 0
        horarios = [
        "6:00 AM - 10:00 AM",
        "10:00 AM - 2:00 PM",
        "2:00 PM - 6:00 PM",
        "6:00 PM - 10:00 PM"
        ]
        salones = {
            "Sputnik": {},
            "Artemis": {},
            "Apollo": {}
        }
        
        campersDisponibles = datos["campers"].copy()
        random.shuffle(campersDisponibles)
        for salon in salones:
            salones[salon] = {}  
            for horario in horarios:
                salones[salon][horario] = [] 

                for i in range(3):  
                    if indiceCamper < len(campersDisponibles):

                        camper = campersDisponibles[indiceCamper]


                        camper["salon"] = salon
                        camper["horario"] = horario

                        salones[salon][horario].append(camper["id"])

                        indiceCamper += 1
            
        # Bucle del menú principal del coordinador
        while booleanito4:
            print("----------------------------------------------")
            print(f"📝 Has ingresado como el/la coordinador/a {coordinadorEncontrado['nombre']} 📝")
            print("1. Crear nueva ruta")
            print("2. Registrar nuevo trainer")
            print("3. Asignar información a camper")
            print("4. Ver notas de camper")
            print("5. Retirar camper")
            print("6. Ver asignacion de salones para campers")
            print("7. Salir del ROL coordinador/a")

            # Se solicita la opción del menú
            opcionCoor = int(input("¿Qué deseas hacer?: "))
            print("----------------------------------------------")
            
            # OPCIÓN 1: Crear nueva ruta
            if opcionCoor == 1:
                # Se pide el nombre de la ruta
                nombreRuta = input("¿Cómo se llama la nueva ruta?: ")

                # Se crea la nueva ruta
                for i in datos["trainers"]:
                    nuevaRuta = {
                        "nombre": nombreRuta,
                        "modulos": []
                    }
                    # Se agrega la ruta a la lista de rutas
                    datos['rutas'].append(nuevaRuta)

                # Se solicita el profesor responsable
                profesorRuta = input("¿A qué profesor le vas a asignar esta nueva ruta?: ")

                # Mensaje de confirmación
                print(f"¡¡¡ Se ha añadido con éxito la ruta {nombreRuta} al trainer {profesorRuta} !!!")

            # OPCIÓN 2: Registrar nuevo trainer
            elif opcionCoor == 2:
                # Se solicitan los datos del nuevo trainer
                nombre = input("¿Cómo se llama el nuevo trainer?: ")
                nuevaID = input("Digite la ID del nuevo trainer: ")
                horario = input("¿Cuál es su horario?: ")
                especialidad = input("¿En qué se especializa?: ")

                # Se crea el diccionario del trainer
                nuevoTrainer = {
                    "id": nuevaID,
                    "nombre": nombre,
                    "horario": horario,
                    "especialidad": especialidad
                }

                # Se agrega el trainer al JSON
                datos["trainers"].append(nuevoTrainer)

                # Mensaje de confirmación
                print(f"✅ El trainer {nombre} fue registrado correctamente")

            # OPCIÓN 3: Asignar información a camper
            elif opcionCoor == 3:
                booleanito5 = True

                # Submenú para gestionar campers
                while booleanito5:
                    print("----------------------------------------------")
                    print("1. Asignar camper a trainer")
                    print("2. Fecha de inicio y graduación")
                    print("3. Jornada del camper")
                    print("4. Volver al menú coordinador")

                    # Se solicita la opción
                    opcionJornadaCamper = int(input("Digite la opción: "))

                    # Asignar camper a trainer
                    if opcionJornadaCamper == 1:
                        camperID = input("ID del camper: ")
                        camper_encontrado = None

                        # Se busca el camper
                        for camper in datos["campers"]:
                            if camper["id"] == camperID:
                                camper_encontrado = camper
                                break

                        # Si no se encuentra el camper
                        if camper_encontrado is None:
                            print("⚠️ Camper no encontrado ⚠️")
                        else:
                            trainerNombre = input(f"Trainer para {camper_encontrado['nombres']}: ")
                            trainer_encontrado = None

                            # Se busca el trainer
                            for trainer in datos["trainers"]:
                                if trainer["nombre"] == trainerNombre:
                                    trainer_encontrado = trainer
                                    break

                            # Si no se encuentra el trainer
                            if trainer_encontrado is None:
                                print("⚠️ Trainer no encontrado ⚠️")
                            else:
                                # Se asigna el trainer al camper
                                camper_encontrado["trainerAsignado"] = trainer_encontrado["nombre"]
                                print("✅ Trainer asignado correctamente")

                    # Asignar fechas
                    elif opcionJornadaCamper == 2:
                        camperID = input("ID del camper: ")
                        camper_encontrado = None

                        # Se busca el camper
                        for camper in datos["campers"]:
                            if camper["id"] == camperID:
                                camper_encontrado = camper
                                break

                        # Si no existe
                        if camper_encontrado is None:
                            print("⚠️ Camper no encontrado ⚠️")
                        else:
                            # Se solicita la fecha de inicio
                            fechaInicio = input("Fecha de inicio (DD/MM/AAAA): ")
                            # Se calcula la fecha de fin
                            fechaFin = calcularFechaFin(fechaInicio)
                            print(f"Inicio: {fechaInicio}")
                            print(f"Graduación estimada: {fechaFin}")

                    # Asignar jornada
                    elif opcionJornadaCamper == 3:
                        # Listas de horarios
                        jornadaMañana = ["6:00 AM - 10:00 AM", "10:00 AM - 2:00 PM"]
                        jornadaTarde = ["2:00 PM - 6:00 PM", "6:00 PM - 10:00 PM"]

                        camperID = input("ID del camper: ")
                        camper_encontrado = None

                        # Se busca el camper
                        for camper in datos["campers"]:
                            if camper["id"] == camperID:
                                camper_encontrado = camper
                                break

                        # Si no existe
                        if camper_encontrado is None:
                            print("⚠️ Camper no encontrado ⚠️")
                        else:
                            # Se solicita la jornada
                            eleccion = input("¿mañana o tarde?: ").lower()

                            # Se asigna la jornada aleatoria
                            if eleccion == "mañana":
                                camper_encontrado["jornada"] = random.choice(jornadaMañana)
                            elif eleccion == "tarde":
                                camper_encontrado["jornada"] = random.choice(jornadaTarde)
                            else:
                                print("⚠️ Opción inválida ⚠️")

                    # Volver al menú coordinador
                    elif opcionJornadaCamper == 4:
                        booleanito5 = False

            # OPCIÓN 4: Ver notas del camper
            elif opcionCoor == 4:
                camperID = input("ID del camper: ")
                for camper in datos["campers"]:
                    if camper["id"] == camperID:
                        print("Práctica:", camper["notaPruebaPractica"])
                        print("Teórica:", camper["notaPruebaTeorica"])
                        break
                else:
                    print("⚠️ Camper no encontrado ⚠️")

            # OPCIÓN 5: Retirar camper
            elif opcionCoor == 5:
                camperID = input("ID del camper a retirar: ")
                for camper in datos["campers"]:
                    if camper["id"] == camperID:
                        camper["estado"] = "inactivo"
                        print(f" Camper {camper['nombres']} retirado")
                        break
                else:
                    print("⚠️ Camper no encontrado ⚠️")
            ## OPCIÓN 6: Ver horario de todos los campers
            elif opcionCoor == 6:
                for salon in salones:
                    print("🏫", salon)

                    for horario in salones[salon]:
                        print("  ⏰", horario)

                        for camper_id in salones[salon][horario]:
                            for camper in datos["campers"]:
                                if camper["id"] == camper_id:
                                    print("     👤 Camper:", camper["nombres"], camper["apellidos"])

                    print("-" * 40)
            
            # OPCIÓN 7: Salir del rol coordinador
            elif opcionCoor == 7:
                print(f"👋 Hasta luego {coordinadorEncontrado['nombre']}")
                booleanito4 = False

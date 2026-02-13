import json

with open("data.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

booleanito = True

while(booleanito== True):
    print("---------------------------")
    print("¡¡Bienvenido a la plataforma de CampusLands!!")
    print("1. Soy un camper 💻")
    print("2. Soy un Trainer 💼")
    print("3. Soy un/a Coordinador/a 📝")
    opcionMenu = int(input("Porfavor ingrese su rol (según el numero): "))
    
    if opcionMenu == 1:
        booleanito2 = True
        while (booleanito2 == True):
            print("----------------------------------------------")
            print("💻 Has ingresado como Camper 💻 ")
            print("1. Ver notas")
            print("2. Ver trainer y ruta asignada")
            print("3. Pruebas y trabajos")
            print("4. Salir del ROL camper")
            opcionCam = int(input("¿Qué deseas hacer?: "))
            print("----------------------------------------------")
            
            if opcionCam == 1:
                pass
            elif opcionCam == 2:
                pass
            elif opcionCam == 3:
                pass
            elif opcionCam == 4:
                pass
    
    elif opcionMenu == 2:
        booleanito3 = True
        while (booleanito3 == True):
            print("----------------------------------------------")
            print("💼 Has ingresado como Trainer 💼 ")
            print("1. Ver notas")
            print("2. Ver trainer y ruta asignada")
            print("3. Pruebas y trabajos")
            print("4. Salir del ROL camper")
            opcionCoor = int(input("¿Qué deseas hacer?: "))
            print("----------------------------------------------")
            
            if opcionCam == 1:
                pass
            elif opcionCam == 2:
                pass
            elif opcionCam == 3:
                pass
            elif opcionCam == 4:
                pass
    
    elif opcionMenu == 3:
        booleanito4 = True
        while (booleanito4 == True):
            print("----------------------------------------------")
            print("📝 Has ingresado como el/la coordinador/a 📝 ")
            print("1. Registrar nuevo camper")
            print("2. Crear nueva ruta")
            print("3. Registrar nuevo trainer")
            print("4. Asignar camper a trainer")
            print("5. Notas de camper")
            print("6. Retirar Camper")
            print("7. Salir del ROL coordinador/a")
            opcionCoor = int(input("¿Qué deseas hacer?: "))
            print("----------------------------------------------")
            
            if opcionCoor == 1:
                pass
            elif opcionCoor == 2:
                pass
            elif opcionCoor == 3:
                pass
            elif opcionCoor == 4:
                pass
            elif opcionCoor == 5:
                pass
            elif opcionCoor == 6:
                pass
            elif opcionCoor == 7:
                pass
            
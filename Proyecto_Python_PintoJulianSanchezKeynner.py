# =========================
# IMPORTACIÓN DE MÓDULOS
# =========================

# Módulo para trabajar con archivos JSON (leer y escribir datos)
import json

# Módulo para generar valores aleatorios
import random

# Importa el archivo coordinador.py
import coordinador

# Importa el archivo trainer.py
import trainer

# Importa el archivo camper.py
import camper

# Importa específicamente la función para iniciar sesión como coordinador
from coordinador import iniciarSesionCoordinador

# Importa específicamente la función para iniciar sesión como trainer
from trainer import iniciarSesionTrainer

# Importa específicamente la función para iniciar sesión como camper
from camper import iniciarSesionCamper


# =========================
# FUNCIÓN PARA CALCULAR FECHA DE FIN
# =========================

# Función que recibe una fecha de inicio y le suma 10 meses
def calcularFechaFin(fechaInicio):
    """Calcula la fecha de fin sumando exactamente 10 meses a la fecha de inicio"""
    try:
        # Separa la fecha usando el carácter "/"
        partes = fechaInicio.split("/")

        # Convierte cada parte de la fecha a número entero
        dia = int(partes[0])
        mes = int(partes[1])
        año = int(partes[2])
        
        # Suma 10 meses a la fecha
        mes += 10
        
        # Si los meses pasan de 12, se ajusta el año
        while mes > 12:
            mes -= 12
            año += 1
        
        # Retorna la fecha final con formato correcto
        return f"{dia:02d}/{mes:02d}/{año}"

    # Si ocurre algún error con el formato de la fecha
    except:
        return "Error en fecha"


# =========================
# CARGA DEL ARCHIVO JSON
# =========================

# Abre el archivo data.json en modo lectura
with open("data.json", "r", encoding="utf-8") as archivo:
    # Carga el contenido del JSON en la variable datos
    datos = json.load(archivo)


# =========================
# MENÚ PRINCIPAL DEL SISTEMA
# =========================

# Variable booleana para controlar el ciclo principal del programa
booleanito = True

# Ciclo principal que mantiene el sistema activo
while booleanito == True:

    # Imprime el encabezado del menú principal
    print("---------------------------")
    print("¡¡Bienvenido a la plataforma de CampusLands!!")
    print("1. Soy un camper 💻")
    print("2. Soy un Trainer 💼")
    print("3. Soy un/a Coordinador/a 📝")

    # Solicita al usuario que seleccione su rol
    opcionMenu = int(input("Porfavor ingrese su rol (según el numero): "))

    # =========================
    # OPCIÓN CAMPER
    # =========================
    if opcionMenu == 1:
        # Llama a la función que maneja el rol de camper
        iniciarSesionCamper()

    # =========================
    # OPCIÓN TRAINER
    # =========================
    elif opcionMenu == 2:
        # Llama a la función que maneja el rol de trainer
        iniciarSesionTrainer()

    # =========================
    # OPCIÓN COORDINADOR
    # =========================
    elif opcionMenu == 3:
        # Llama a la función que maneja el rol de coordinador
        iniciarSesionCoordinador()


# =========================
# FINALIZACIÓN DEL PROGRAMA
# =========================

# Cambia la variable a False para finalizar el programa
booleanito = False

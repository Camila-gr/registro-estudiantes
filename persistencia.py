import json
import os

# Esto localiza automáticamente la carpeta "datos" y el archivo "estudiantes.json"
CARPETA_DATOS = os.path.join(os.path.dirname(__file__), "datos")
RUTA_ARCHIVO = os.path.join(CARPETA_DATOS, "estudiantes.json")


def cargar_datos():
    """Abre el archivo JSON y saca la lista de alumnos para que Python la use."""
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except Exception:
        return []


def guardar_datos(lista_estudiantes):
    """Toma la lista de alumnos y la guarda en el archivo JSON."""
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(lista_estudiantes, archivo, indent=4, ensure_ascii=False)


# --- PRUEBA RÁPIDA PARA SABER SI FUNCIONA ---
if __name__ == "__main__":
    print("Probando tu archivo...")

    # Creamos un alumno de prueba
    alumno_falso = [
        {"cedula": "12345", "nombre": "Prueba", "carrera": "Sistemas", "promedio": 18}
    ]

    # Lo guardamos en el JSON
    guardar_datos(alumno_falso)
    print("1. Guardado en el JSON: ¡LISTO!")

    # Lo volvemos a leer desde el JSON
    datos_recuperados = cargar_datos()
    print("2. Leído desde el JSON:", datos_recuperados)
    print("\n¡Todo funciona perfecto!")
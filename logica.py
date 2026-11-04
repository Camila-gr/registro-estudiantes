#Importamos funciones
from persistencia import cargar_datos, guardar_datos


#---------- Funcion Registrar estudiante-----------------------------
def registrar_estudiante():
    print("\n-----REGISTRAR ESTUDIANTE----")
    estudiantes = cargar_datos()
    
    #Ingresamos la cédula
    cedula = input("Ingrese la cédula del estudiante: ").strip()
    if not cedula:
        print("Error la cédula no puede estar vacía.")
        return
    
    #validamos si existe o no la cédula
    for est in estudiantes:
        if est["cedula"] == cedula:
            print("Error: ya existe un estudiante registrado con esa cédula.")
            return
        
    #Ingresamos el nombre y la carrera 
    nombre = input("Ingrese el nombre completo: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return

    carrera = input("Ingrese la carrera: ").strip()
    if not carrera:
        print("Error: La carrera no puede estar vacía.")
        return
    
    #Ingresamos el promedio 
    try:
        #Intenta convertir la entrada del usuario a un número decimal (float
        nota = float(input("Ingrese la nota final (0 a 20): "))
        
        # Valida que la nota se encuentre dentro del rango permitido
        if nota < 0 or nota > 20:
            print("Error: La nota debe estar en un rango de 0 a 20.")
            return
    except ValueError:
        # Atrapa el error si el usuario ingresa letras o caracteres no numéricos,
        # evitando que el programa colapse o se cierre inesperadamente
        print("Error: Debe ingresar un valor numérico válido para la nota.")
        return
    
    #creamos nuevo diccionario
    nuevo_estudiante = {
            "cedula": cedula,
            "nombre": nombre,
            "carrera": carrera,
            "nota": nota
        }
    
    #Añadimos el diccionario y guardamos datos 
    estudiantes.append(nuevo_estudiante)
    guardar_datos(estudiantes)
    print("¡Estudiante registrado exitosamente!")
    
    

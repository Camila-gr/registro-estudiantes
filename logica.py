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


    #---------- Funcion listar estudiantes-----------------------------
def listar_estudiantes():
    print("\n---- LISTA DE ESTUDIANTES ----")
    estudiantes = cargar_datos()
    
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    for est in estudiantes:
        print(f"Cédula: {est['cedula']} | Nombre: {est['nombre']} | Carrera: {est['carrera']} | Nota: {est['nota']}")


    #---------- Funcion buscar estudiante-----------------------------
def buscar_estudiante():
    print("\n---- BUSCAR ESTUDIANTE ----")
    estudiantes = cargar_datos()
    
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    #Ingresar la cedula a buscar
    cedula_buscar = input("Ingrese la cédula del estudiante a buscar: ").strip()
    encontrado = False
    
    for est in estudiantes:
        if est['cedula'] == cedula_buscar:
            print(f"\n¡Estudiante encontrado!")
            print(f"Cédula: {est['cedula']}")
            print(f"Nombre: {est['nombre']}")
            print(f"Carrera: {est['carrera']}")
            print(f"Nota: {est['nota']}")
            encontrado = True
            break

    if not encontrado:
        print("No se encontró ningún estudiante con esa cédula.")

    
        
    print("¡Estudiante registrado exitosamente!")


#----------funcion modificar datos----------
def modificar_estudiante():
    print("\n--- MODIFICAR ESTUDIANTE ---")
    estudiantes = cargar_datos()
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

#ingresar la cedula a buscar
    cedula = input("Ingrese la cédula del estudiante que desea modificar: ").strip()
    encontrado = False

    for est in estudiantes:
        if est['cedula'] == cedula:
            encontrado = True
            print(f"Estudiante actual: {est['nombre']} - Nota: {est['nota']}")
            
            #nuevos datos
            nuevo_nombre = input("Nuevo nombre (deje en blanco para no cambiar): ").strip()
            if nuevo_nombre:
                est['nombre'] = nuevo_nombre

            nueva_carrera = input("Nueva carrera (deje en blanco para no cambiar): ").strip()
            if nueva_carrera:
                est['carrera'] = nueva_carrera

            nueva_nota_str = input("Nueva nota (deje en blanco para no cambiar): ").strip()
            if nueva_nota_str:
                try:
                    nueva_nota = float(nueva_nota_str)
                    if 0 <= nueva_nota <= 20:
                        est['nota'] = nueva_nota
                    else:
                        print("Nota fuera de rango (0-20). No se modificó la nota.")
                except ValueError:
                    print("Valor inválido para la nota. No se modificó la nota.")

            guardar_datos(estudiantes)
            print("¡Estudiante modificado exitosamente!")
            break

#---------funcion eliminar datos-----------
        
def eliminar_estudiante():
    print("\n--- ELIMINAR ESTUDIANTE ---")
    estudiantes = cargar_datos()
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    # pide la cédula del estudiante para buscar
    cedula = input("Ingrese la cédula del estudiante a eliminar: ").strip()
    
    #filtra la lista: creando otra lista con los estudiantes que tengan la cedula diferente a la que se busca
    estudiantes_filtrados = [est for est in estudiantes if est['cedula'] != cedula]

    if len(estudiantes_filtrados) == len(estudiantes):
        print("No se encontró ningún estudiante con esa cédula.")
    else:
        guardar_datos(estudiantes_filtrados)
        print("¡Estudiante eliminado exitosamente!")

    if not encontrado:
        print("No se encontró ningún estudiante con esa cédula.")
    
    

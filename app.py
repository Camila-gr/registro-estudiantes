# app.py
# Menú principal del Sistema de Registro de Estudiantes.
# Ejecutar con: python app.py

from logica import (
    registrar_estudiante,
    listar_estudiantes,
    buscar_estudiante,
    modificar_estudiante,
    eliminar_estudiante,
    reporte_promedio_y_aprobados,
)


def mostrar_menu():
    print("\n========== REGISTRO DE ESTUDIANTES ==========")
    print("1. Registrar estudiante")
    print("2. Listar estudiantes")
    print("3. Buscar estudiante")
    print("4. Modificar estudiante")
    print("5. Eliminar estudiante")
    print("6. Reporte: promedio y aprobados")
    print("7. Salir")
    print("=============================================")


def main():
    opcion = ""

    # El ciclo se repite hasta que el usuario elija la opción 7
    while opcion != "7":
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ").strip()

        try:
            if opcion == "1":
                registrar_estudiante()
            elif opcion == "2":
                listar_estudiantes()
            elif opcion == "3":
                buscar_estudiante()
            elif opcion == "4":
                modificar_estudiante()
            elif opcion == "5":
                eliminar_estudiante()
            elif opcion == "6":
                reporte_promedio_y_aprobados()
            elif opcion == "7":
                print("\n¡Gracias por usar el sistema! Hasta luego.")
            else:
                print("Error: opción inválida. Escriba un número del 1 al 7.")
        except Exception as error:
            # Evita que el programa se cierre por un error inesperado
            print(f"\nNo se pudo completar la operación: {error}")
            print("El programa sigue funcionando.")


# Solo se ejecuta cuando abrimos app.py directamente
if __name__ == "__main__":
    main()

# Sistema de Registro de Estudiantes

Proyecto 1 — Lenguaje de Programación III · UNEFA, Ingeniería de Sistemas · Período 2026-II · Docente: Ing. David Marín

| Dato | Detalle |
|---|---|
| **Sistema** | Sistema de Registro de Estudiantes |
| **Tema** | **Tema #3 — Registro de estudiantes** (cédula, nombre, carrera y nota) |
| **Persistencia** | **Opción A — JSON** (`datos/estudiantes.json`) |
| **Lenguaje** | Python 3, solo biblioteca estándar (`json`, `os`) |
| **Ejecución** | `python app.py` |
| **Integrantes** | José Giménez · Frida Osteicoechea · Maria Trómpiz · Camila Gauna · Christian Lugo |
| **Uso de IA** | Declarado en la sección «Uso de IA» |

---

## Cómo ejecutar

```bash
python app.py
```

En Windows: `py app.py`. No requiere `pip install` ni librerías externas; la carpeta `datos/` con `estudiantes.json` ya viene en el proyecto.

Menú: 1 registrar · 2 listar · 3 buscar · 4 modificar · 5 eliminar · 6 reporte · 7 salir. Al elegir 7 el programa termina y los datos quedan guardados.

**El reporte del tema (opción 6)** muestra el total de estudiantes, el promedio general con 2 decimales y el listado de aprobados (nota ≥ 10, escala 0–20).

---

## Estructura y responsabilidades

```text
├── app.py                 # Menú y ciclo principal
├── logica.py              # Reglas: registrar, listar, buscar, modificar, eliminar, reporte
├── persistencia.py        # Leer y guardar el JSON
├── datos/estudiantes.json # Los datos
└── README.md
```

`app.py` → `import logica` → `import persistencia`. Cada archivo hace una sola cosa (modularidad): `app.py` solo llama funciones, `logica.py` valida y decide cuándo guardar, `persistencia.py` es el único que abre el archivo.

---

## Persistencia (Opción A: JSON)

```python
CARPETA_DATOS = os.path.join(os.path.dirname(__file__), "datos")
RUTA_ARCHIVO = os.path.join(CARPETA_DATOS, "estudiantes.json")
```

`__file__` y `dirname()` ubican la carpeta del script, así funciona aunque se ejecute desde otra ruta.

Formato del archivo: una **lista** con un **diccionario** por estudiante.

```json
[{ "cedula": "12345", "nombre": "Prueba", "carrera": "Sistemas", "nota": 18.0 }]
```

- Claves fijas: `cedula`, `nombre`, `carrera`, `nota`. Si se renombra una, aparece `KeyError`.
- La cédula es texto para no perder ceros a la izquierda (`"01234567"`).
- **`cargar_datos()`**: abre en modo `"r"` con `encoding="utf-8"` y usa `json.load()` dentro de `try/except`; si el archivo no existe o está dañado devuelve `[]` y el programa arranca vacío.
- **`guardar_datos(lista)`**: abre en modo `"w"` (sobrescribe todo) y usa `json.dump(..., indent=4, ensure_ascii=False)`, que deja el archivo legible y conserva tildes y `ñ`.

**Regla de oro:** cargar al inicio de cada operación y guardar al final de la que modifica datos.

---

## Funciones de `logica.py`

| Función | Qué hace |
|---|---|
| `registrar_estudiante()` | Valida cédula (no vacía y no repetida), nombre, carrera y nota (`float()` + rango 0–20); agrega con `append()` y guarda |
| `listar_estudiantes()` | Avisa si no hay datos; si hay, imprime una línea por estudiante con un f-string |
| `buscar_estudiante()` | Recorre comparando la cédula con una bandera `encontrado` y `break` |
| `modificar_estudiante()` | Dejar un campo en blanco conserva el valor anterior; la nota se vuelve a validar |
| `eliminar_estudiante()` | Comprensión de listas que copia todos menos el de la cédula indicada; si el tamaño no cambia, no se encontró |
| `reporte_promedio_y_aprobados()` | `sum()` de las notas ÷ cantidad, y aprobados con nota ≥ 10 |

`app.py`: `mostrar_menu()` imprime las 7 opciones y `main()` las repite con `while opcion != "7"`, comparando texto (`"1"`, `"2"`, …) porque `input()` devuelve texto. El `try/except Exception` del menú evita que el programa se cierre ante un error inesperado.

---

## Validaciones y manejo de errores

| Situación | Respuesta del programa |
|---|---|
| Cédula vacía | `Error la cédula no puede estar vacía.` |
| Cédula repetida | `Error: ya existe un estudiante registrado con esa cédula.` |
| Nombre o carrera vacíos | `Error: El nombre no puede estar vacío.` / `Error: La carrera no puede estar vacía.` |
| Nota con letras o vacía | `Error: Debe ingresar un valor numérico válido para la nota.` |
| Nota fuera de 0–20 | `Error: La nota debe estar en un rango de 0 a 20.` |
| Buscar o eliminar una cédula inexistente | `No se encontró ningún estudiante con esa cédula.` |
| Opción de menú inválida | `Error: opción inválida. Escriba un número del 1 al 7.` y vuelve al menú |
| El JSON no existe | `cargar_datos()` devuelve `[]` |
| Error inesperado | `app.py` lo captura y el programa sigue |

---

## Pruebas mínimas

1. Registrar un estudiante válido → se guarda.
2. Repetir la cédula → error de duplicado.
3. Enter vacío en cédula/nombre/carrera → error de campo vacío.
4. Nota `abc` y nota `25` → error de tipo y de rango.
5. Listar → aparece el estudiante.
6. Buscar una cédula inexistente → mensaje de no encontrado.
7. Modificar solo la nota → nombre y carrera se conservan.
8. Eliminar → desaparece de la lista y del JSON.
9. Reporte → total, promedio con 2 decimales y aprobados.
10. Salir (7), abrir de nuevo y listar → **los datos siguen ahí**.

---

## Notas sobre el código actual

1. Al final de `buscar_estudiante()` se imprime `¡Estudiante registrado exitosamente!`, un mensaje heredado del registro.
2. El bloque `if __name__ == "__main__":` de `persistencia.py` guarda un alumno de prueba con la clave `"promedio"` y escribe sobre el JSON real, por eso **no debe ejecutarse** `python persistencia.py` con datos cargados.
3. `modificar_estudiante()` no avisa cuando la cédula no existe; vuelve al menú sin cambios.

---

## Uso de IA

El grupo usó inteligencia artificial como apoyo para entender conceptos, explicar errores y revisar la redacción de este README. Todo el código fue probado con datos correctos e incorrectos y es comprendido por los integrantes, que pueden explicar y modificar cualquier parte del programa.

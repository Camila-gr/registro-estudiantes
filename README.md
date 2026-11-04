# Sistema de Registro de Estudiantes

Proyecto del Primer Corte · **Lenguaje de Programación III** (UNEFA) · Período 2026-II

- **Tema:** Registro de estudiantes (cédula, nombre, carrera y nota).
- **Persistencia:** Opción A — **JSON** (`datos/estudiantes.json`).
- **Lenguaje:** Python 3, solo biblioteca estándar (`json`, `os`).
- **Integrantes:** _completar con los nombres del grupo._
- **Uso de IA:** _completar en una o dos líneas._

---

## Cómo ejecutar

```bash
python app.py
```

Si no funciona en Windows: `py app.py`.

Menú: 1 registrar · 2 listar · 3 buscar · 4 modificar · 5 eliminar · 6 reporte · 7 salir.
Los datos quedan en `datos/estudiantes.json` y siguen ahí al cerrar y volver a abrir.

---

## Los archivos y su responsabilidad

| Archivo | Se encarga de… |
|---|---|
| `app.py` | Menú y ciclo principal. Solo llama funciones; no valida ni guarda. |
| `logica.py` | Reglas: registrar, listar, buscar, modificar, eliminar y reporte. |
| `persistencia.py` | Leer y escribir el JSON. |
| `datos/estudiantes.json` | Los datos: una lista de diccionarios, uno por estudiante. |

Cadena de imports: `app.py` → `import logica` → `import persistencia`. Cada archivo hace una sola cosa: eso es la **modularidad**.

---

## Cómo funciona, en orden

1. `app.py` muestra el menú con `mostrar_menu()` dentro de un `while`.
2. El usuario escribe una opción y se ejecuta el `if/elif` correspondiente.
3. Esa función de `logica.py` empieza con `cargar_datos()` (trae la lista del JSON).
4. Pide los datos con `input()`, los valida y modifica la lista.
5. Si hubo cambios, llama a `guardar_datos(estudiantes)` para reescribir el JSON.
6. Vuelve al menú hasta que se elija la opción 7.

**Regla de oro:** cargar al inicio de cada operación y guardar al final de la que modifica algo. Sin `guardar_datos`, el cambio se pierde al cerrar.

---

## `persistencia.py`

```python
CARPETA_DATOS = os.path.join(os.path.dirname(__file__), "datos")
RUTA_ARCHIVO = os.path.join(CARPETA_DATOS, "estudiantes.json")
```

- `__file__` es la ruta de `persistencia.py`; `dirname` toma su carpeta. Así el programa funciona aunque se ejecute desde otra ubicación.

**`cargar_datos()`**: abre el JSON en modo `"r"` con `encoding="utf-8"`, lo convierte con `json.load` y devuelve la lista. Todo va en `try/except`: si el archivo no existe (primera ejecución) o está dañado, devuelve `[]` y el programa arranca vacío en vez de cerrarse.

**`guardar_datos(lista_estudiantes)`**: abre en modo `"w"` (sobrescribe todo) y escribe con `json.dump(..., indent=4, ensure_ascii=False)`. `indent=4` deja el archivo legible; `ensure_ascii=False` conserva tildes y `ñ`. El `with open(...)` cierra el archivo solo.

**`if __name__ == "__main__":`**: el bloque de prueba corre únicamente con `python persistencia.py`, no cuando `logica.py` la importa. Ojo: ese bloque **sobrescribe el JSON** y usa la clave `"promedio"` en vez de `"nota"`.

---

## `datos/estudiantes.json`

```json
[
    { "cedula": "12345", "nombre": "Prueba", "carrera": "Sistemas", "nota": 18.0 }
]
```

- `[ ]` = lista; `{ }` = diccionario.
- Las claves deben llamarse igual que en el código: `cedula`, `nombre`, `carrera`, `nota`. Si una clave cambia de nombre, Python lanza `KeyError`.
- La cédula va como texto para no perder ceros a la izquierda (`"01234567"`).

---

## `logica.py`

**`registrar_estudiante()`** — pide cédula, nombre, carrera y nota; valida cada campo y guarda.
- Cédula: no vacía (`if not cedula`) y no repetida (recorre la lista comparando `est["cedula"] == cedula`).
- Nombre y carrera: no vacíos.
- Nota: `float()` dentro de `try/except ValueError` y rango `0` a `20`.
- Crea el diccionario, lo agrega con `append()` y llama a `guardar_datos()`.
- Cualquier validación fallida hace `return` antes de guardar.

**`listar_estudiantes()`** — si la lista está vacía, avisa; si no, recorre con `for` e imprime cada estudiante con un f-string.

**`buscar_estudiante()`** — recorre comparando la cédula, usa una bandera `encontrado = False` que pasa a `True` y un `break` al encontrar. Si termina y sigue en `False`, muestra "No se encontró...".

**`modificar_estudiante()`** — busca por cédula y pregunta nombre, carrera y nota; si se deja en blanco, el valor anterior se conserva. La nota se vuelve a validar (`0 <= nota <= 20`). Guarda y hace `break`.

**`eliminar_estudiante()`** — comprensión de listas que copia todos **menos** el de la cédula indicada:
```python
estudiantes_filtrados = [est for est in estudiantes if est['cedula'] != cedula]
```
Si `len(estudiantes_filtrados) == len(estudiantes)`, nadie coincidió → "No se encontró...". Si no, guarda la lista filtrada.

**`reporte_promedio_y_aprobados()`** — el reporte del tema:
- `sum(est['nota'] for est in estudiantes)` suma las notas.
- Promedio = suma ÷ `len(estudiantes)` (se dividió solo después de comprobar que hay estudiantes).
- Aprobados: comprensión de listas con `est['nota'] >= 10` (escala 0–20).
- `{promedio:.2f}` muestra 2 decimales.

---

## `app.py`

**`mostrar_menu()`** — solo imprime las 7 opciones (así no se repiten los `print`).

**`main()`**:
```python
opcion = ""
while opcion != "7":
    mostrar_menu()
    opcion = input("Seleccione una opción (1-7): ").strip()
    try:
        if opcion == "1":
            registrar_estudiante()
        ...
```
- Se compara con textos (`"1"`), porque `input()` siempre devuelve texto.
- El `else` avisa "opción inválida" y el ciclo continúa.
- El `except Exception as error` es la red de seguridad: muestra el error y el menú sigue, cumpliendo "el programa no se cierra ante errores".
- `if __name__ == "__main__": main()` arranca el menú solo al ejecutar `python app.py`.

---

## Validaciones que ya están resueltas

| Situación | Respuesta del programa |
|---|---|
| Cédula, nombre o carrera vacíos | Mensaje de error y no guarda |
| Cédula repetida | "Ya existe un estudiante con esa cédula" |
| Nota con letras o vacía | `ValueError` capturado, mensaje y no guarda |
| Nota menor que 0 o mayor que 20 | "Debe estar en un rango de 0 a 20" |
| Buscar/eliminar/modificar una cédula inexistente | "No se encontró ningún estudiante con esa cédula" |
| Opción del menú inválida | "Opción inválida" y vuelve al menú |
| El JSON no existe todavía | `cargar_datos()` devuelve `[]` |
| Error inesperado en una operación | `app.py` lo captura y el programa continúa |

---

## Errores conocidos (corregir antes de entregar)

1. **`NameError` al eliminar** — al final de `eliminar_estudiante()` hay `if not encontrado:`, pero `encontrado` no existe en esa función. El borrado sí se guarda, pero se muestra un error. **Solución:** borrar esas dos líneas.
2. **`KeyError: 'nota'`** — el registro del JSON usa `"promedio"`. **Solución:** renombrar esa clave a `"nota"` (o borrar ese registro de prueba).
3. **Mensaje en la función equivocada** — "¡Estudiante registrado exitosamente!" está en `buscar_estudiante()`. **Solución:** moverlo al final de `registrar_estudiante()`.
4. **Modificar sin aviso** — si la cédula no existe, `modificar_estudiante()` termina en silencio. **Solución:** agregar `if not encontrado: print("No se encontró...")` después del `for`.

---

## Pruebas mínimas

1. Registrar un estudiante válido → se guarda.
2. Registrar la misma cédula → error de duplicado.
3. Enter en cédula/nombre/carrera → error de campo vacío.
4. Nota `abc` y nota `25` → error de tipo y de rango.
5. Listar → aparece el estudiante.
6. Buscar una cédula que no existe → "No se encontró...".
7. Modificar solo la nota → nombre y carrera se conservan.
8. Eliminar → desaparece de la lista.
9. Reporte → total, promedio con 2 decimales y aprobados.
10. Salir (7), volver a abrir y listar → **los datos siguen ahí** (persistencia).

---

## Preguntas clave de la defensa

**¿Por qué la cédula es texto?** No se opera matemáticamente con ella y no se pierden ceros a la izquierda.

**¿Qué pasa si el JSON no existe?** `cargar_datos()` captura el error y devuelve `[]`; el programa inicia sin estudiantes.

**¿Por qué cargar en cada función y no una sola vez?** Para trabajar siempre con lo último guardado en el archivo.

**¿Qué hace `guardar_datos`?** Sobrescribe el JSON completo con la lista que recibe (modo `"w"`), por eso se le pasa la lista entera.

**¿Diferencia lista vs diccionario?** Lista = colección ordenada (todos los estudiantes); diccionario = pares clave-valor (un estudiante).

**¿Cómo se evita duplicar cédulas?** Recorriendo la lista antes de guardar y saliendo con `return` si ya existe.

**¿Cómo funciona eliminar?** Copia la lista sin el estudiante indicado; si el tamaño no cambia, no se encontró.

**¿Qué hace `try/except`?** Evita que un error cierre el programa; se usa al convertir la nota, al leer el JSON y como red de seguridad del menú.

**¿Por qué `while opcion != "7"`?** Porque repite el menú hasta que el usuario elige salir.

**¿Por qué se compara con `"1"` y no con `1`?** Porque `input()` devuelve texto.

---

## Declaración de uso de IA

_Completar antes de la entrega. Ejemplo:_

> El grupo usó IA como apoyo para explicar conceptos, revisar errores y revisar la redacción del README. Todo el código fue probado y comprendido por los integrantes.

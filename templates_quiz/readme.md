# 🧪 Prueba - Fundamentos de Programación en Python

En esta prueba validaremos nuestros conocimientos para codificar un programa en Python utilizando las herramientas vistas en el curso, así como aplicar estilos y convenciones de programación como **indentación**, **estructura de código** y **uso de diccionarios**.

> Para ello, utilizarás el archivo de apoyo:  
> **`Prueba - Fundamentos de programación en Python (Apoyo)`**

---

## 📘 Descripción

¡Llegó el gran momento! Te has unido a **ADL Desarrolladores**, una entidad dedicada a crear apps entretenidas, con un equipo que sigue buenas prácticas de desarrollo de software.

El equipo ha sido asignado para desarrollar una **App de trivia interactiva en Python**, con preguntas clasificadas por nivel de dificultad:

- Básica
- Intermedia
- Avanzada

El jugador definirá cuántas preguntas quiere responder por nivel. Para ganar, debe responder correctamente todas.

Las preguntas deben:

- Aparecer en **orden aleatorio**
- Tener **alternativas mezcladas** en cada ejecución

Debido a la complejidad, el **Project Manager** ha generado un **backlog** con tareas específicas, las cuales se desarrollarán paso a paso.

---

## 🧱 Estructura del código

Cada subtarea se desarrollará como un script en Python, que incluirá:

```python
# Definición de funciones de la funcionalidad
def funcion():
    pass

if __name__ == '__main__':
    # Test entregado en cada requerimiento
```

El archivo `preguntas.py` incluye tres diccionarios:

- `preguntas_basicas`
- `preguntas_intermedias`
- `preguntas_avanzadas`

Cada diccionario contiene **3 preguntas**. Cada pregunta es un diccionario con:

- Un `enunciado` (string)
- Una lista de `alternativas`, cada una como: `[texto, indicador]`, donde `1` indica la respuesta correcta.

> 📝 Todas las preguntas tienen la alternativa correcta en la posición `'alt_2'`.  
> Se recomienda modificar las preguntas y alternativas para simular una trivia real.

Además, hay un diccionario `pool_preguntas` que categoriza las preguntas por nivel:

```python
pool_preguntas[nivel][pregunta_n]
```

---

## 📂 Archivos y Funcionalidades

### 1. `validador.py`

- Crear la función `validate(opciones, eleccion)`
- Si la elección no está en las opciones, mostrar:

  ```
  Opción no válida, ingrese una de las opciones válidas:
  ```

- Repetir hasta que se ingrese una válida
- Retornar la opción ingresada

> 💡 Tip: Usar `not in` para verificar pertenencia

---

### 2. `level.py`

- Crear función `choose_level(n_pregunta, cantidad_por_nivel)`
- Comportamiento esperado:

  - Si `cantidad_por_nivel == 2`:
    - Preguntas 1-2 → Básicas
    - Preguntas 3-4 → Intermedias
    - Preguntas 5-6 → Avanzadas

  - Si `cantidad_por_nivel == 3`:
    - Preguntas 1-3 → Básicas
    - Preguntas 4-6 → Intermedias
    - Preguntas 7-9 → Avanzadas

- La función retorna el **nivel de dificultad** correspondiente

---

### 3. `shuffle.py`

- Crear función `shuffle_alt(pregunta)`
- Usar `random.shuffle()` para mezclar alternativas
- Retorna las alternativas mezcladas

---

### 4. `question.py`

- Crear función `choose_q(dificultad)`
- Extraer preguntas según dificultad desde `preguntas.py`
- Escoger una **pregunta no repetida**
- Eliminar la pregunta del conjunto
- Retornar:
  1. El enunciado
  2. Las alternativas mezcladas

---

### 5. `print_preguntas.py`

- Crear función `print_pregunta(enunciado, alternativas)`
- Imprimir:

  ```
  ¿Pregunta?

  A. Alternativa 1  
  B. Alternativa 2  
  C. Alternativa 3  
  D. Alternativa 4
  ```

- No retorna nada, solo imprime

---

### 6. `verify.py`

- Crear función `verificar(alternativas, eleccion)`
- Si la elección es correcta:

  ```
  Respuesta Correcta
  ```

  → Retorna `True`

- Si es incorrecta:

  ```
  Respuesta Incorrecta
  ```

  → Retorna `False`

---

### 7. `main.py` (esqueleto incluido en el archivo de apoyo)

Debes completar las siguientes funcionalidades:

- Validar si iniciar el programa (opción 0 → terminar con: `"Nos vemos pronto!"`)
- Validar número de preguntas por nivel
- Determinar nivel según `n_pregunta` y cantidad por nivel
- Obtener enunciado y alternativas
- Imprimir enunciado y alternativas
- Validar y verificar respuesta
- Preguntar si continuar

---

## ✅ Requerimientos de Evaluación

1. Crear y manipular variables y estructuras de datos correctamente  
2. Crear funciones con distintos parámetros y buenas prácticas  
3. Modularizar adecuadamente en múltiples archivos  
4. Valida tipos de datos y testea las funcionalidades correctamente

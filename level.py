def choose_level(n_pregunta, p_level):
   
    # Establecer valor por defecto
    level = 'basicas'  # valor por defecto
    # Logica para 1 pregunta por nivel que determina nivel de dificultad
    if p_level == 1:
        if n_pregunta == 1:
            level = 'basicas'
        elif n_pregunta == 2:
            level = 'intermedias'
        else:
            level = 'avanzadas'
    # Logica para 2 preguntas por nivel que determina nivel de dificultad
    elif p_level == 2:
        if n_pregunta <= 2:
            level = 'basicas'
        elif n_pregunta <= 4:
            level = 'intermedias'
        else:
            level = 'avanzadas'
    # Logica para 3 preguntas por nivel que determina nivel de dificultad
    elif p_level == 3:
        if n_pregunta <= 3:
            level = 'basicas'
        elif n_pregunta <= 6:
            level = 'intermedias'
        else:
            level = 'avanzadas'
    # Devuelve el nivel determinado según el número de pregunta y preguntas por nivel       
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2))  # básicas
    print(choose_level(3, 2))  # intermedias
    print(choose_level(7, 2))  # avanzadas
    print(choose_level(4, 3))  # intermedias
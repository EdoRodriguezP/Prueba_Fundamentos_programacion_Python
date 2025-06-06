import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    
    #Accede al diccionario preguntas segun dificultad(nivel)
    preguntas = p.pool_preguntas[dificultad]
    
    # Usa la variable global opciones que contiene los numeros disponibles de cada nivel
    global opciones
    
    # Elige aleatoriamente un numero de pregunta
    n_elegido = random.choice(opciones[dificultad])
    
    # eliminarla del ambiente global para no escogerla de nuevo
    opciones[dificultad].remove(n_elegido)
    
    # escoger enunciado y alternativas mezcladas
    pregunta = preguntas[f'pregunta_{n_elegido}']
    
    # Llama a la funcion suffle_alt para traer las alternativas mescladas.
    alternativas = shuffle_alt(pregunta) 
    
    # Retorna Tupla con enunciado de la pregunta y sus alternativas mezclada
    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
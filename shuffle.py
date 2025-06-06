import preguntas as p
import random

# La funcion recibe un diccionario de preguntas
def shuffle_alt(pregunta):
    
    # obtiene la lista de alternativas formato texto-valor
    alternativas = pregunta['alternativas']
    
    # mezcla aleatoriamente las alternativas
    random.shuffle(alternativas)
    
    # Retorna lista de alternativas mezcladas
    return pregunta['alternativas']

if __name__ == '__main__':
    # si se ejecuta el  programa varias veces las alternativas debieran aparecer en distinto orden
    print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1'])) 
    # a modo de ejemplo
    # [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]
import preguntas as p

# La funjcion recibe los parametros "enunciado y alternativas en formato texto valor"
def print_pregunta(enunciado, alternativas):
    
    # Imprime enunciado con saltos de linea
    print(f"\n{enunciado}\n")
    
    # diccionario de letras con sus numeros de mapeo
    letras = {0:'A', 1:'B', 2:'C', 3:'D'}
    
    # Bucle para pares de indice y valorpara cada alternativa
    for index, alternativa in enumerate(alternativas):
        
        # Imprime letras y alternativas
        print(f"{letras[index]}. {alternativa[0]}")

if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4
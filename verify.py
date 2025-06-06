import preguntas as p


def verificar(alternativas, eleccion):
    
    # Convierte la letra elegida en un numero de indice
    eleccion = ['a', 'b', 'c','d'].index(eleccion)
    
    # Toma el valor u compara si el valoer es correcto. devuelve True/False
    correcto = alternativas[eleccion][1] == 1    # Toma el valor u compara si el valoer es correcto. devuelve True/False
    
    # Imprimir mensaje según el resultado, Si correcto es True imprime respuesta
    if correcto:          
        print('Respuesta Correcta')
    else:
        print('Respuesta Incorrecta')
        
    # Retorna correcto sea True o False   
    return correcto


if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)








def validate(opciones, eleccion):
    
    # recibe 2 parametros, una lista de opciones y la eleccion de las preguntas
    while eleccion not in opciones:
        
        # Si parametro no esta imprime opciones y solicita nueva respuesta
        print(f"\nOpción no válida. Las opciones son: {', '.join(opciones)}")
        eleccion = input('Ingresa una Opción válida: ').lower()
        
    # Retorna la eleccion
    return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
    
    

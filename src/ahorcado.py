import random
def cargar_palabras(ruta):
    '''
    Recibe la ruta de un fichero de texto que contiene una palabra por línea y devuelve
    dichas palabras en una lista.
    '''
    with open(ruta, encoding='utf-8') as f:
        res = []
        for linea in f:
            res.append(linea.strip()) # strip() elimina los espacios en blanco y saltos de línea al principio y al final
        return res
    
def elegir_palabra(palabras):
    '''
    Elige la palabra a adivinar:
    - Selecciona una palabra aleatoria de la lista 'palabras'
    - Devuelve la palabra seleccionada
    Ayuda: 
    - La función 'random.choice' del paquete 'random' recibe una lista de opciones y 
      devuelve una de ellas seleccionada aleatoriamente.
    '''
    palabra_aleatoria = random.choice(palabras)
    return palabra_aleatoria

def enmascarar_palabra(palabra, letras_probadas):
    '''
    Enmascarar la palabra:
    - Inicializar una lista vacía. 
    - Recorrer cada letra de la palabra, añadiendola a la lista 
      si forma parte de las letras_probadas, o añadiendo un '_' en caso contrario. 
    - Devuelve una cadena concatenando los elementos de la lista (ver 'Ayuda')
    Ayuda: 
    - Utilice el método join de las cadenas. Observe el siguiente ejemplo:
        ' '.join(['a','b','c']) # Devuelve "a b c"
    '''
    resultado = []
    for letra in palabra:
        if letra in letras_probadas:
            resultado.append(letra)

        else:
            resultado.append('_')

    resultado = " ".join(resultado) 

    return resultado 

def pedir_letra(letras_probadas):
    
    '''
    
    Pedir la siguiente letra:
    - Pedirle al usuario que escriba la siguiente letra por teclado
    - Comprobar si la letra indicada ya se había propuesto antes y pedir otra si es así
    - Considerar las letras en minúsculas aunque el usuario las escriba en mayúsculas
    - Devolver la letra
    Ayuda:
    - La función 'input' permite leer una cadena de texto desde la entrada estándar
    - El método 'lower' aplicado a una cadena devuelve una copia de la cadena en minúsculas
    '''   
    letra = input('Introduce una letra: ')
    while letra in letras_probadas: 
        print('Esa ya la has elegido')
        letra = input('Introduce una letras: ')

    else:
        return letra.lower() 
    
def comprobar_letra(palabra_secreta, letra:str):
    '''
    Comprobar letra:
    - Comprobar si la letra está en la palabra secreta o no
    - Mostrar el mensaje correspondiente informando al usuario
    - Devolver True si estaba y False si no
    ''' 
    if letra.lower() in palabra_secreta:
        return True
    else:
        return False
    
def comprobar_palabra_completa(palabra_secreta, letras_probadas):
    '''
    Comprobar si se ha completado la palabra:
    - Comprobar si todas las letras de la palabra secreta han sido propuestas por el usuario
    - Devolver True si es así o False si falta alguna letra por adivinar
    '''
    letras_correctas = True
    for letra in palabra_secreta:
        if letra not in letras_probadas:
            return False 
    return True

def ejecutar_turno(palabra_secreta, letras_probadas):
    '''
    Ejecutar un turno de juego:
    - Mostrar la palabra enmascarada
    - Pedir la nueva letra
    - Comprobar si la letra está en la palabra (acierto) o no (fallo)
    - Añadir la letra al conjunto de letras probadas
    - Devolver True si la letra fue un acierto, False si fue un fallo
    Ayuda:
    - Recuerda las funciones que ya has implementado para mostrar la palabra, pedir la letra y comprobarla
    '''
    palabra = enmascarar_palabra(palabra_secreta, letras_probadas)
    print(f"Palabra: {palabra}")

    letra = pedir_letra(letras_probadas)
    letras_probadas.add(letra)

    if comprobar_letra(palabra_secreta, letra):
        return True
    else:
        return False

def jugar(max_intentos, palabras):
    '''
    Completar una partida hasta que el jugador gane o pierda:
    - Mostrar mensaje de bienvenida
    - Elegir la palabra secreta a adivinar
    - Inicializar las variables del juego (letras probadas e intentos fallidos)
    - Ejecutar los turnos de juego necesarios hasta finalizar la partida, y en cada turno:
      > Averiguar si ha habido acierto o fallo
      > Actualizar el contador de fallos si es necesario
      > Comprobar si se ha superado el número de fallos máximo
      > Comprobar si se ha completado la palabra
      > Mostrar el mensaje de fin adecuado si procede o el número de intentos restantes
    '''
    print("¡Bienvenido al juego del ahorcado!")
    
    palabra_secreta = elegir_palabra(palabras)
    letras_probadas = set()
    intentos_fallidos = 0
    
    while True:
        acierto = ejecutar_turno(palabra_secreta, letras_probadas)
        
        if not acierto:
            intentos_fallidos += 1
            print(f"Fallaste. Te quedan {max_intentos - intentos_fallidos} intentos.")
        
        if intentos_fallidos >= max_intentos:
            print(f"¡Has perdido! La palabra era: {palabra_secreta}")
            break
        
        if comprobar_palabra_completa(palabra_secreta, letras_probadas):
            print(f"¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
            break
        
        #palabra_enmascarada = enmascarar_palabra(palabra_secreta, letras_probadas)
        #print(f"Palabra actual: {palabra_enmascarada}")

    print("Fin del juego.")

    # Iniciar el juego(final del ejercicio)
if __name__ == "__main__":
    palabras = cargar_palabras("data/palabras_ahorcado.txt")
    jugar(6, palabras)
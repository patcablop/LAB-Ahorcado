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
import imp


import string

def codifico(frase):
    """ recibe una frase, la convierte en lista, codificamos esta frase y devolvemos un iterable"""
    frase.split()
    codigo = map(lambda x: chr(ord(x)+1), frase)
    return codigo

def decodifico(codigo):
    """ genera un nuevo string con los elementos del iterable que recibe por parametro"""
    nuevo = ""
    for elem in nuevo_codigo:
        nuevo = nuevo + elem
    return nuevo

frase = input("ingrese una frase: ")
nuevo_codigo= codifico(frase)
print(decodifico(nuevo_codigo)) 

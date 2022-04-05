import string

def codifico(frase):
    """ recibe una frase, la convierte en lista, codificamos esta frase y devolvemos un iterable"""
    frase.split()
    codigo = map(lambda x: chr(ord(x)+1), frase)
    return codigo

frase = input("ingrese una frase: ")
nuevo_codigo= codifico(frase)
separador = ""
nueva_frase = separador.join(nuevo_codigo)
print(nueva_frase)

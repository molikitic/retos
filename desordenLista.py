from random import randint as rd
def desordenaLista(lista):
    ln = []
    while len(lista)!=0:
        nr = rd(0,len(lista)-1)
        ln.append(lista.pop(nr))
    return ln
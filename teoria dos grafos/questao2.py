from grafo123 import Grafo

def quebraTexto(variavel):
    aux = variavel.split(", ")
    return aux

def quebraAresta(variavel):
    listaAux = quebraTexto(variavel)
    aresta = ''
    listaAresta = []
    for i in listaAux:
        for j in i:
            if j is not "(":
                aresta+=j
            if j == "(":
                listaAresta.append(aresta)
                aresta = ''
                break
    return listaAresta

def quebraLigacao(variavel):
    listaAux = quebraTexto(variavel)
    listaLigacao = []
    for i in listaAux:
        for j in range(len(i)):
            if i[j] is "(":
                ligacao = i[j+1:len(i)-1]
                listaLigacao.append(ligacao)
                continue
    return listaLigacao

def criaDicionario(listaChave, listaValor):
    dicionario = {}
    for i in range(len(listaChave)):
        dicionario[listaChave[i]] = listaValor[i]
    return dicionario
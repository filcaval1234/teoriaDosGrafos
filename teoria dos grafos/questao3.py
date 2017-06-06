from grafo123 import Grafo

grafo = Grafo(N=["a","b","c","d","e","f"], A={"a1":"a-b", "a2":"b-d", "a3": "b-c", "a3":"c-e", "a4":"c-f", "a5":"b-c", "a6": "b-a"})
ligacao = grafo.A
#print(ligacao)

def retornaSegundoNo(string):
    segundoNo = ''
    for i in range(len(string)):
        if string[i] == '-':
            segundoNo = string[i+1:]
    return segundoNo

def retornaPrimeiroNo(string):
    primeiroNo = ''
    for i in range(len(string)):
        if string[i] == '-':
            primeiroNo = string[:i - 1]
    return primeiroNo

def naoAdjacente(dicionarioLigacao):
    aresta = []
    nAdj = []
    traco = "-"
    for i in dicionarioLigacao:
        aresta.append(dicionarioLigacao[i])
    for i in range(len(aresta)):
        recbPop = aresta.pop()
        recbPop = recbPop.split("-")
        for i in recbPop:
            for j in aresta:
                if i not in j:
                    if i+"-"+j[j.index(traco)+1:] not in nAdj and j[j.index(traco)+1:]+"-"+i not in nAdj:
                        nAdj.append(i+"-"+j[j.index(traco)+1:])

    return nAdj

#print(naoAdjacente(ligacao))

def criaListaLigacao(dicionarioLigacao):
    aresta = []
    for i in dicionarioLigacao:
        aresta.append(dicionarioLigacao[i])
    return aresta

def inverteString(string):
    return retornaSegundoNo(string)+"-"+retornaPrimeiroNo(string)

def selfAdjacente(dicionarioLigacao):
    listaAresta = criaListaLigacao(dicionarioLigacao)
    print(listaAresta)
    condicao = False
    traco = "-"

    for i in listaAresta:
        primeiro = i[:i.index(traco)]
        ultimo = i[i.index(traco)+1:]
        for i in listaAresta:
            if ultimo+"-"+primeiro == i:
                condicao = True
                break
    return condicao

#print(selfAdjacente(ligacao))

def arestaParalelas(dicionarioLigacao):
    listaAresta = criaListaLigacao(dicionarioLigacao)
    print(listaAresta)
    condicao = False
    traco = "-"
    for i in listaAresta:
        ultimo = i[i.index(traco)+1:]
        print(ultimo)
        for j in listaAresta:
            if ultimo == j[:j.index(traco)]:
                condicao = True
                break
    return condicao
print(arestaParalelas(ligacao))
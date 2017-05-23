from grafo import Grafo

grafo = Grafo(N=["a","b","c","d","e","f"], A={"a1":"a-b", "a2":"b-d", "a3": "b-c", "a3":"c-e", "a4":"c-f"})
ligacao = grafo.A
print(ligacao)

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
    for i in dicionarioLigacao:
        aresta.append(dicionarioLigacao[i])
    for i in aresta:
        for j in aresta:
            if i[0] not in j:
                nAdj.append(i[0]+"-"+retornaSegundoNo(j))
    return nAdj

print(naoAdjacente(ligacao))

def criaListaLigacao(dicionarioLigacao):
    aresta = []
    for i in dicionarioLigacao:
        aresta.append(dicionarioLigacao[i])
    return aresta

def inverteString(string):
    return retornaSegundoNo(string)+"-"+retornaPrimeiroNo(string)

def selfAdjacente(dicionarioLigacao):
    listaAresta = criaListaLigacao(dicionarioLigacao)
    condicao = False
    for i in listaAresta:
        for j in range(1,len(listaAresta)):
            if i == inverteString(listaAresta[j]):
                condicao =  True
                return condicao
        if condicao is True: break
    return condicao
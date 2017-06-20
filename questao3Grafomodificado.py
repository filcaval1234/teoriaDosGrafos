from grafo123 import Grafo
n = ["a", "b", "c", "d", "e"]
a = {"a1":"a-b", "a2":"b-c", "a3":"c-d", "a4":"a-e"}
grafo = Grafo(N=n, A=a);
matriz = grafo.colocaMatriz(a, n)
print(type(matriz))

def naoAdjacente(n, matriz):
    listaNaoAdjacente = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == 0:
                listaNaoAdjacente.append(n[i]+"_"+n[j])
    print(listaNaoAdjacente)

def existeLaço(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if (i == j and matriz[i][j] == 1):
                return True
    return False

def verificaParalelo(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == matriz[j][i]:
                return True
    return False

def verificaGrau(matriz, vertice, n):
    indiceVertice = n.index(vertice)
    return matriz[indiceVertice].count(1)

def grafoCompleto(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if (j > i) and matriz[i][j] == 0:
                return False
    return True

#-----------------------e esse trosso------------------------
def conexo(matriz, listaDeConbinacao):

    for k in range(len(matriz)):
        arestaAdja = arestaExistente(matriz, k)

        for i in range(len(arestaAdja[1])):
            if [arestaAdja[0], arestaAdja[1][i]] in listaDeConbinacao:
                del(listaDeConbinacao[listaDeConbinacao.index([arestaAdja[0], arestaAdja[1][i]])])
                if len(listaDeConbinacao) == 0:
                    return True

    for j in range(len(listaDeConbinacao)):
        if procura(listaDeConbinacao[j][1],listaDeConbinacao[j][0]) == True:
            listaDeConbinacao[j] = '#'

    if listaDeConbinacao.count("#") == len(listaDeConbinacao):
        return True
    else: return False

                
#---------------------em cima--------------------------------
    
def procura(indiceDeProcura,procurado):
    a = False
    l = arestaExistente(matriz,indiceDeProcura,indiceDeProcura)
    if procurado in l[1]:
        a = True
        return a
    else:
        try:
            novoIndiceDeProcura = l[1][0]
        except:
            return a
        del(l[1][0])
        a = procura(indiceDeProcura=novoIndiceDeProcura,procurado=procurado)
    return a

def conbinacoes(matriz):
    #esse trosso retorna um lista com todas as conbinacoes de caminhos possiveis
    # retorna algo do tipo [x,y]
    conbinacao = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i is not j and [j,i] not in conbinacao:
                conbinacao.append([i,j])
    return conbinacao

def arestaExistente(matriz, index, numeroHaSerRetirado=-1):
    #esse trosso vai retornar algo do tipo [0,[1,2,3,5]]
    arestaExiste = [index,[]]
    for i in range(len(matriz)):
        if matriz[index][i] == 1:
            arestaExiste[1].append(i)
        #if matriz[index].count(1) == 0:
        if matriz[i][index] == 1:
            arestaExiste[1].append(i)
        if numeroHaSerRetirado in arestaExiste[1]:
            del(arestaExiste[arestaExiste.index(numeroHaSerRetirado)])
    return arestaExiste

#naoAdjacente(n, matriz)
for i in matriz:
    print(i)
conbinac = conbinacoes(matriz)
print(conexo(matriz, listaDeConbinacao=conbinac))
#print(conbinac)
#print(procura(4,0))
#print(verificaGrau(matriz, "a", n))

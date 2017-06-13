from grafo123 import Grafo
n = ["a", "b", "c", "d", "e"]
a = {"a1":"a-b", "a2":"b-c", "a3":"d-e", "a4":"a-e"}
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
def conexo(matriz, listaDeConbinacao, k=0):
    if len(listaDeConbinacao) is 0:
        return "ALGUMA COISA"
    arestaAdja = arestaExistente(matriz,k)
    #if [b,c] not in listacomnb:
    #   fazer alguma coisa
    # else:
    for i in range(len(arestaAdja[1])):
        if listaDeConbinacao[k] is [arestaAdja[0], arestaAdja[1][i]]:
            del(listaDeConbinacao[k])
        #precisa de maisn coisa!!!!!!!!!!!!!!!!!
    conexo(matriz, listaDeConbinacao, k+1)
                
#---------------------em cima--------------------------------
    
    

def conbinacoes(matriz):
    #esse trosso retorna um lista com todas as conbinacoes de caminhos possiveis
    # retorna algo do tipo [x,y]
    conbinacao = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            conbinacao.append([i,j])
    return conbinacao

def arestaExistente(matriz, index):
    #esse trosso vai retornar algo do tipo [0,[1,2,3,5]]
    arestaExiste = [index,[]]
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j == index and matriz[j] == 1:
                arestaExiste[1].append(j)
    return arestaExiste

naoAdjacente(n, matriz)
print(verificaGrau(matriz, "a", n))

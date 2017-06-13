from grafo123 import Grafo
n = ["a", "b", "c", "d", "e"]
a = {"a1":"a-b", "a2": "b-c", "a3":"b-d", "a4":"d-e"}
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



def caminhoAresta(valor, listacaminho, listaindex,tamanho, i=1):
    if i == len(listaindex):
        return
    if valor[1] == listaindex[i][0]:
        if len(listacaminho) is not tamanho:
            tiraRepetido(listacaminho, valor, listaindex[i])
            excluirepetido(listacaminho)
        caminhoAresta(listaindex[i], listacaminho, listaindex,tamanho,i+1)
    caminhoAresta(valor, listacaminho, listaindex,tamanho, i+1)
    return

def tiraRepetido(lista, valor1, valor2):
    if valor1 not in lista:
        lista.append(valor1)
    if valor2 not in lista:
        lista.append(valor2)

def excluirepetido(lista):
    for i in range(len(lista)-1):
        if lista[i][0] == lista[i+1][0]:
            lista[i] = ["-","-"]
    for i in range(len(lista)):
        try:
            if lista[i] == ["-","-"]:
                del(lista[i])
        except:
            continue

def encontraUM(matriz):
    listaIndex = []
    existeLigacao = 1
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == existeLigacao:
                listaIndex.append([i,j])
    return listaIndex

def salvaCaminho(x,y,n):
    return  n[x]+"-"+n[y]

for i in matriz:
    print(i)
listaind = encontraUM(matriz)
listacaminho = []
caminhoAresta(listaind[0], listacaminho, listaind,4, 1)
#print(encontraUM(matriz))
excluirepetido(listacaminho)
print(listacaminho)


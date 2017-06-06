from grafo123 import Grafo
n = ["a", "b", "c", "d", "e"]
a = {"a1":"a-b", "a2":"b-c", "a3":"e-e"}
grafo = Grafo(N=n, A=a)
matriz = grafo.InserirMatrizRepresentacao(a, n)

def naoAdjacente(n, matriz):
    listaNaoAdjacente = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == 0:
                listaNaoAdjacente.append(n[i]+"_"+n[j])
    print(listaNaoAdjacente)

def existeLaco(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if (i == j and matriz[i][j] == 1):
                return True
    return False

def verificaParalelo(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == 1 and matriz[j][i] == 1:
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
def verificaConexo(matriz):
    count = 0
    for i in range(len(matriz)):
        count += matriz[i].count(1)
    if count >= len(matriz) -1:
        return True
    return False

def printMatriz(matriz,n):
        grafo_str = '  '
        for k in n:
            grafo_str += k+" "
        for i in range(len(n)):
            grafo_str += "\n"+n[i]
            for j in range(len(matriz)):
                grafo_str += " "+str(matriz[i][j])
        return grafo_str

#print(verificaParalelo(matriz))
print(printMatriz(matriz,n))

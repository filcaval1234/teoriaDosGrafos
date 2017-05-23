from grafo123 import Grafo
from questao2 import *
caracterInvalido = ['(',')','-']

while True:
    while True:
        no = input('digite todos os nós separados por virgula\n'
                   'OBS.: os nós não podem ser declarados com "(", ")" e "-"')
        if caracterInvalido[0] in no or caracterInvalido[1] in no or caracterInvalido[2] in no :
            continue
        else: break

    listaNo = quebraTexto(no)
    grafo = Grafo(N=listaNo)

    cont = 1
    while cont is not 0:
        aresta = input('digite o nome da aresta seguido da ligação no formato abaixo;\n'
                       'a1(J-C), a2(C-E), a3(C-E), ...')
        listaLigacao = quebraLigacao(aresta)
        for i in listaLigacao:
            if grafo.arestaValida(aresta=i):
                cont = 0
    listaAresta = quebraAresta(aresta)
    listaNo = quebraTexto(no)

    grafo = Grafo(N=listaNo, A=criaDicionario(listaChave=listaAresta, listaValor=listaLigacao))
    print(grafo)
# a, b, c, d, e
# a1(a-b), a2(b-c), a3(d-e), a4(a-e)
from grafo123 import Grafo
from questao2 import *
grafo = Grafo(N=['J','C','E','P','M','T','Z'], A={'a1':'J-C','a2':'C-E','a3':'C-E',
                                                  'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T',
                                                  'a8': 'M-T', 'a9':'T-Z'})
print(grafo)


#__________________________________________________________questão 2________________________



aresta1 = quebraAresta('aa df1(J-C), a675672(C-E), a3(C-E)')
ligacao = quebraLigacao('a1(J-C), a2(as dfC-E), a3(C-E)')

print(aresta1,"--",ligacao)

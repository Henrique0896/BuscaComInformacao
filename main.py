from buscas import buscaLargura, buscaProfundidadeLI, buscaAEstrela, buscaGulosa
from manipularArquivo import lerArquivo, escreverArquivo, escreverArquivo2

estadoInicial, estadoFinal = lerArquivo('estadoInicial.txt', 'estadoFinal.txt')

#caminho1 = buscaLargura(estadoInicial, estadoFinal)

#caminho2 = buscaProfundidadeLI(estadoInicial, estadoFinal)

caminho3 = buscaGulosa(estadoInicial, estadoFinal)

caminho4 = buscaAEstrela(estadoInicial, estadoFinal)


escreverArquivo2('caminho.txt', caminho3, caminho4)
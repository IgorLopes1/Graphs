from graph import Graph
import time

while True:
    file = input("Informe o arquivo (0 para sair): ")
    #se o arquivo informado for 0 encerra no programa
    if file == "0":
        break
    #tratamento de excessão para caso o arquivo não seja encontardo,
    #caso seja encontrado abre o arquivo e armazena na variavel "labirinto"
    try:
        with open(file, "r") as file:
            labirinto = [list(line.strip()) for line in file]
    except FileNotFoundError:
        print("Arquivo não encontrado!")
        continue
    #cria um grafo passando o labirinto como argumento do construtor
    print("Processando...")
    graph = Graph(labirinto)

    #procura pela entrada do labirinto representada por "S"
    for i in range(len(labirinto)):
        for j in range(len(labirinto[0])):
            if labirinto[i][j] == "S":
                entrada = (i, j)
                break
    #inicia o timer para medir o tempo de execução da busca em profundidade
    inicio = time.time()
    #realiza a busca em profundidade e imprime o caminho
    print("Caminho:", graph.dfs(entrada, set(), []))
    #finaliza o timer e imprime o tempo de execução em segundos
    fim = time.time()
    print("Tempo de execução:", fim - inicio, "segundos")





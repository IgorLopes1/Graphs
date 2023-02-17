class Graph:
    def __init__(self, labirinto):
        self.labirinto = labirinto
        self.graph = self.cria_grafo()


    #Função cria um grafo com todos os elementos do labirinto.txt que são diferentes de "#"
    def cria_grafo(self):
        graph = {}
        linhas = len(self.labirinto)
        colunas = len(self.labirinto[0])
        #percorre o arquivo labirinto por todas as linhas e colunas
        for v in range(linhas):
            for u in range(colunas):
                no = (v, u)
                adjacente = []
                #se for diferente de "#" adiciona a posição (v,u) no grafo
                if self.labirinto[v][u] != "#":

                    if v > 0 and self.labirinto[v - 1][u] != "#" :
                        adjacente.append((v - 1, u))
                    if u > 0 and self.labirinto[v][u - 1] != "#":
                        adjacente.append((v, u - 1))

                    if v < linhas - 1 and self.labirinto[v + 1][u] != "#":
                        adjacente.append((v + 1, u))
                    if u < colunas - 1 and self.labirinto[v][u + 1] != "#":
                        adjacente.append((v, u + 1))

                #grafo na posição (u,v) recebe adjacente
                graph[no] = adjacente
                #retorna o grafo
        return graph

    #Procura a menor rota saindo do no de entrada até encontrar o nó E
    def dfs(self, no, visitado, no_pai):
        if self.labirinto[no[0]][no[1]] == "E":
            return [no]
        visitado.add(no)
        for adjacente in self.graph[no]:
            if adjacente not in visitado:
                caminho = self.dfs(adjacente, visitado, no)
                if caminho is not None:
                    return [no] + caminho
        return None
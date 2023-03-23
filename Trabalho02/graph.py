import networkx as nx
import pandas as pd


def cria_grafo_csv(file_path):
    df = pd.read_csv(file_path)

    graph = nx.DiGraph()

    graph.add_node("s", weight=0)
    graph.add_node("t", weight=0)

    for i, row in df.iterrows():
        graph.add_node(row["CÓDIGO"], weight=0)
        graph.add_edge("s", row["CÓDIGO"], weight=0)

    for i, row in df.iterrows():
        if isinstance(row["PRÉ-REQUISITO"], str):
            pre_reqs = row["PRÉ-REQUISITO"].split(";")
        else:
            pre_reqs = []

        for pre_req in pre_reqs:
            pre_req = pre_req.strip()
            graph.add_edge(row["CÓDIGO"], pre_req, weight=int(row["DURACAO"]))

    for i, row in df.iterrows():
        graph.add_edge(row["CÓDIGO"], "t", weight=int(row["DURACAO"]))

    return graph



def bellman_ford_caminho_critico(graph, df):
    dist = {node: float('-inf') for node in graph.nodes()}
    prev = {node: None for node in graph.nodes()}

    dist["s"] = 0

    for _ in range(len(graph.nodes()) - 1):
        for u, v, weight in graph.edges(data="weight"):
            if dist[u] + weight > dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
    longest_path = []
    node = "t"
    while node != "s":
        longest_path.append(node)
        node = prev[node]
    longest_path.append("s")
    reversed_path = list(reversed(longest_path))

    disciplinas = dict(zip(df["CÓDIGO"], df["NOME"]))
    caminho_critico = [disciplinas[codigo] for codigo in reversed_path if codigo in disciplinas][::-1]

    return caminho_critico, dist["t"]

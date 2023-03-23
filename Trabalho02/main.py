import pandas as pd
from graph import cria_grafo_csv, bellman_ford_caminho_critico

while True:
    file = input("\nInforme o arquivo (0 para sair): ")
    if file == "0":
        break
    try:
        print("Processando...")
        df = pd.read_csv(file)
        grafo = cria_grafo_csv(file)
        caminho, duracao = bellman_ford_caminho_critico(grafo, df)

        print(f'Caminho crítico : {caminho}')
        print(f'Duração mínima : {duracao} periodos')
    except FileNotFoundError:
        print("Arquivo não encontrado!")
        continue

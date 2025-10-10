import csv
path_arquivo = "vendas.csv"

def ler_csv(nome_arquivo: str) -> list[dict]:
    """
    Funcao que le um arquivo csv e retorna uma lista de dicionarios
    """
    lista = []
    with open(nome_arquivo, mode = "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)

    return lista

def filtrar_produtos_nao_entregues(lista: list[dict]) -> float:
    """
    Funcao que filtra produtos onde entrega = True
    """
    lista_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_produtos_filtrados.append(produto)
    return lista_produtos_filtrados

lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
print(produtos_entregues)
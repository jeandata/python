from datetime import date
from typing import Dict,Any

informacoes_livro: Dict = {}

livro1: Dict[str, Any] = {
        "Titulo": "Fundametos de Engenharia de dados",
        "Autor":  "Reis, Housley",
        "Ano_publicado": "22/07/2021"
}

lista_livros = []

lista_livros.append(livro1)

print(lista_livros)

lista_livros_dict: dict = {
        "Livro1":{
        "Titulo": "Fundametos de Engenharia de dados",
        "Autor":  "Reis, Housley",
        "Ano_publicado": "22/07/2021"},

        "Livro2":{
        "Titulo": "Fundametos de Engenharia de dados 2",
        "Autor":  "Reis, Housley",
        "Ano_publicado": "22/07/2024"}

}

print(lista_livros_dict["Livro1"]["Titulo"])
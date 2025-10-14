import time
from controller import obter_cotacao, add_cotacao


def main():
    while True:
        moeda_schema = obter_cotacao()
        if moeda_schema:
            print(f"Adicionando a nova cotação da criptomoeda:{moeda_schema.criptomoeda} ao banco de dados")
            add_cotacao(moeda_schema)
        else:
            print(f"Não foi possível adicionar a nova cotação")
        time.sleep(10)

if __name__ == "__main__":
    main()
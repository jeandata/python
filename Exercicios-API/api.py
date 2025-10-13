import requests
from pydantic import BaseModel, ConfigDict

class MoedaSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    criptomoeda: str
    moeda: str
    valor: float

def cotacao() -> MoedaSchema:
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    data = response.json()
    dados = data['data'].values() 
    #Dicionários em Python têm métodos próprios para extrair suas partes. 
    # Existe um método para pegar as chaves (.keys()), um para pegar os pares de chave-valor (.items()), 
    # e um para pegar apenas os valores (.values()).
    dado_final = list(dados)
    return MoedaSchema(criptomoeda = dado_final[1], valor = dado_final[0], moeda = dado_final[2])

if __name__ == "__main__":
    print(cotacao())

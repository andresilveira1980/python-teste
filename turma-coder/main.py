# Extrair dados da API
import requests

url = 'https://api.thedogapi.com/v1'

response = requests.get(url=url, headers=None)

if response.status_code == 200:
    data=response.json()
    print('extração feita com sucesso.')
else:
    print('A comunicação com a API falhou.')
# Transformar os dados
print(data)
# (LOAD) Carga dos dados em uma nova fonte de dados


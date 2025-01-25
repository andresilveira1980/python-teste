# Extrair os dados da API
import requests

url = 'https://api.thedogapi.com/v1/breeds'

response = requests.get(url=url, headers=None)

if response.status_code == 200:
    print(response.json())
else:
    print('Não foi possível se comunidar com a API dos cachorrinhos')
#Transformar os dados


#(LOAD) Carga dos dados em uma nova fonte de dados
name = "André Silveira"

for i in range(4):
    print(name)

nomes = []

while True:
    nome = input('Digite um nome próprio (ou digite sair para finalizar):')
    if nome.lower() == 'sair':
        break
    nomes.append(nome)

for nome in nomes:
    print(nome)
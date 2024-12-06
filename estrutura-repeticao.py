name = "André Silveira"

for i in range(4):
    print(name)

soma = 0
i = 1
while i < 6:
    numero = int(input('Digite um número: '))
    soma = soma + numero
    i =i + 1
print(soma)


soma = 0
for i in range(5):
    numero = int(input('Digite um valor '))
    soma = numero + soma

print(soma) 


nomes = []

while True:
    nome = input('Digite um nome próprio (ou digite sair para finalizar):')
    if nome.lower() == 'sair':
        break
    nomes.append(nome)

for nome in nomes:
    print(nome)


print ('----------------------Programa que soma números --------------------------------')
print()


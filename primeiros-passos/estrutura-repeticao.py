name = "André Silveira"

for i in range(4):
    print(name)

soma = 0
i = 1
while i < 6:
    numero = int(input('Digite um número: '))
    soma += numero
    i +=1
print(soma)


soma = 0
for i in range(5):
    numero = int(input('Digite um valor '))
    soma += numero

print(soma) 


nomes = []

while True:
    nome = input('Digite um nome próprio (ou digite sair para finalizar):')
    if nome.lower() == 'sair':
        break
    nomes.append(nome)

for nome in nomes:
    print(nome)

print('-----------------------Programa que conta pares ------------------------')
print()

contaPares = 0
i = 1
for i in range(5):
    i+=1
    valor = int(input('Digite um número: '))
    if valor%2 == 0:
        contaPares += 1
print('Você digitou ', contaPares, 'números pares')    
        
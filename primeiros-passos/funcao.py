print('-----------------FUNCOES INTERNAS -------------------------')

lista = [12, 13]
print(lista)
print(sum(lista))
for elemento in lista:
    print(elemento)

print(max(lista))
print(min(lista))

print('-------------------CRIANDO FUNCOES-----------------------------------')

def mensagem():
    print('Função Criada')

mensagem()

def dobro(valor):
    return valor * 2
    

dobro(14)

numeroDigitado = int(input('Digite um número: '))
dobro(numeroDigitado)

print ('O dobro de ', numeroDigitado, ' é ', dobro(numeroDigitado))
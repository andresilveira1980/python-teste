def numAnterior(numero):
    return numero - 1

def produto(multiplicando, multiplicador):
    return multiplicando * multiplicador

def fatorialNumero(numero):
    fatorial = 1
    while numero > 0:
        fatorial = produto(fatorial, numero)
        numero = numAnterior(numero)
    return fatorial

numeroDigitado = int(input('Digite um número inteiro: '))
print('o fatorial do número digitado é: ', fatorialNumero(numeroDigitado))
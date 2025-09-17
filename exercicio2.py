# Programa em Python que lê dois números inteiros e exibe o quadrado da diferença do primeiro valor pelo segundo.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

diferenca = n1-n2
resultado = diferenca ** 2

print('O quadrado da diferença é: ', resultado)

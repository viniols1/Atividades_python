# Exercício 1 - Operações matemáticas com dois números inteiros.

n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))

print('soma:', n1+n2)
print('Subtração:', n1-n2)
print('Multiplicação:', n1*n2)

if n2 != 0:
    print('Divisão: ', n1/n2)
    print('Divisão truncada: ', n1//n2)
    print('Resto:', n1 % n2)
else:
    print('Divisão: impossível dividir por zero')
    print('Divisão truncada: impossível dividir por zero')
    print('Resto: impossível dividir por zero')

print('Exponenciação', n1**n2)

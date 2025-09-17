# Calculadora básica que calcula os gastos mensais e fornece o valor que o cliente gastou e o valor que sobrou.

salario = int(input('Digite o valor do seu salário: '))
aluguel = int(input('Digite o valor do seu alugel: '))
compras_de_casa = int(input('Digite o valor das compras de casa: '))
conta_de_agua = int(input('Digite o valor da sua fatura de energia: '))
conta_de_luz = int(input('Digite o valor da sua fatura de agua: '))
internet = int(input('Digite o valor da sua fatura de internet:'))
conta_de_telefone = int(input('Digite o valor da sua fatura de telefone: '))

soma = aluguel+compras_de_casa+conta_de_agua + \
    conta_de_luz+internet+conta_de_telefone
subtracao = salario-aluguel-compras_de_casa - \
    conta_de_agua-conta_de_luz-internet-conta_de_telefone

print('Com base nos calculos, você gastou:', soma)
print('Com base nos calculos o valor que sobra é:', subtracao)

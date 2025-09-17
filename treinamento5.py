# Calculadora que soma o faturamento mensal durante o ano e forneçe a média final.

jan = float(input('Digite o faturamento de Janeiro: '))
fev = float(input('Digite o faturamento de Fevereiro: '))
mar = float(input('Digite o faturamento de Março: '))
abr = float(input('Digite o faturamento de Abril: '))
mai = float(input('Digite o faturamento de Maio: '))
jun = float(input('Digite o faturamento de Junho: '))
jul = float(input('Digite o faturamento de Julho: '))
ago = float(input('Digite o faturamento de Agosto: '))
set = float(input('Digite o faturamento de Setembro: '))
out = float(input('Digite o faturamento de Outubro: '))
nov = float(input('Digite o faturamento de Novembro: '))
dez = float(input('Digite o faturamento de Dezembro: '))

soma = jan+fev+mar+abr+mai+jun+jul+ago+set+out+nov+dez
divisao = soma/12

print(f'A soma total do faturamento anual é de R$: {divisao:,.2f}')
print(f'A média total do faturamento de ano é de R$: {divisao:,.2f}')

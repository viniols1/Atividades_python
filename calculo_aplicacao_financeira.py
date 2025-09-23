# Uma instituição financeira necessita de um programa que calcula o valor futuro de uma aplicação financeira com base em diferentes cenários de investimento, como a escolha entre uma conta poupança, um Certificado de Depósito Bancário (CDB) ou Tesouro Direto. O programa deve considerar diferentes taxas de juros e períodos de investimento e será útil para quem quer comparar diferentes opções de investimento e entender como o valor de uma aplicação pode crescer ao longo do tempo com diferentes taxas de juros.

# O programa deve solicitar ao usuário o código do tipo de investimento (1- poupança, 2- CDB ou 3- Tesouro Direto), o valor inicial da aplicação e o prazo do investimento em meses.

# As taxas de juros mensais são definidas para cada tipo de investimento:

# - Poupança: 0,5% ao mês.

# - CDB: 0,8% ao mês.

# - Tesouro Direto: 1% ao mês.

# Este programa deve calcula o valor futuro da aplicação usando a fórmula de juros compostos:

# Valor Futuro = Valor Inicial *  (1  + Taxa de Juros)

tipo_investimento = int(input(
    'Informe o código do investimento (1- Poupança, 2- CDB, 3- Tesouro direto): '))
valor_inicial = float(input('Informe o valor inicial da aplicação: R$ '))
prazo_meses = int(input('Informe o prazo do investimento em meses: '))

if tipo_investimento == 1:
    taxa_juros = 0.005
elif tipo_investimento == 2:
    taxa_juros = 0.008
elif tipo_investimento == 3:
    taxa_juros = 0.01
else:
    print('Tipo de investimento inválido.')
    exit()

valor_futuro = valor_inicial * (1 + taxa_juros) ** prazo_meses
print(f'O valor futuro da aplicação é: R$ {valor_futuro:.2f}')

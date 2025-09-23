# Programa em Python solicitado por uma empresa para cálculo do valor da parcela que o cliente deve pagar devido a uma compra.
# A loja tem as seguintes regras:
# Quando o cliente paga o valor da compra à vista ela concede um desconto de 10% no valor da compra;
# Quando o cliente paga no cartão de crédito, em uma vez, ela concede um desconto de 5% no valor da compra;

# Para desenvolver o programa leve em consideração que serão informados o valor da compra e um código numérico, que representa a opção da forma de pagamento escolhida pelo cliente.

valor_compra = float(input("Informe o valor da compra: "))
codigo_pagamento = int(input(
    "Informe o código da forma de pagamento (1 - À vista, 2 - Cartão de crédito): "))

if codigo_pagamento == 1:
    valor_parcela = valor_compra * 0.9
    print(f"Valor da parcela à vista: R$ {valor_parcela:.2f}")
elif codigo_pagamento == 2:
    valor_parcela = valor_compra * 0.95
    print(f"Valor da parcela no cartão de crédito: R$ {valor_parcela:.2f}")
elif codigo_pagamento == 3:
    valor_parcela = valor_compra / 5
    print(f"Valor da parcela em 5 vezes: R$ {valor_parcela:.2f}")
elif codigo_pagamento == 4:
    valor_parcela = valor_compra * 1.15 / 10
    print(f"Valor da parcela em 10 vezes: R$ {valor_parcela:.2f}")
else:
    print("Código de pagamento inválido.")

peso = float(input())

if peso > 50.0:
    excesso = peso - 50.0
    multa = excesso * 4.0
    print(f"{excesso:.2f}")
    print(f"{multa:.2f}")
else:
    bonificacao = peso * 1.0
    print(f"{bonificacao:.2f}")

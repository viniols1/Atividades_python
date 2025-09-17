# Exercício 3 - Divisão de prêmio entre ganhadores em que o primeiro colocado recebe 46% do prêmio, o segundo recebe 32% e o terceiro recebe o restante.

# valor total do prêmio

premio_total = 780.000
primeiro = premio_total * 0.46
segundo = premio_total * 0.32
terceiro = premio_total - (primeiro + segundo)

print(f"Primeiro colocado receberá: R$ {primeiro:.3f}")
print(f"Segundo colocado receberá: R$ {segundo:.3f}")
print(f"Terceiro colocado receberá: R$ {terceiro:.3f}")

import math

area = float(input())
litros = area / 3
latas = math.ceil(litros / 18)
preco = latas * 120.00

print(latas)
print(f"{preco:.2f}")

import random

valores = [random.randint(50, 100) for _ in range(500)]
pares = sum(1 for v in valores if v % 2 == 0)
impares = sum(1 for v in valores if v % 2 != 0)

print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)

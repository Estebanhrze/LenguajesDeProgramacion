sucursales = [f"Sucursal_{i+1}" for i in range(25)]
ventas = [
    1200, 1500, 1800, 900, 2100,
    3000, 2500, 4000, 3500, 2800,
    5000, 4500, 6000, 3200, 2700,
    1000, 800, 1500, 2000, 3100,
    2200, 1400, 2600, 3300, 3700
]

promedio = sum(ventas) / len(ventas)

print("Promedio de ventas:", promedio)
print("Sucursales con ventas mayores al promedio:")
for i in range(len(sucursales)):
    if ventas[i] > promedio:
        print(sucursales[i], "-", ventas[i])

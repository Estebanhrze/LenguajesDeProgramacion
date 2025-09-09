valores = []
for i in range (10):
    valor_ingresado = float(input(f"Ingrese el valor {i +1}: "))
    valores.append(valor_ingresado)
suma = sum(valores)

promedio = suma / len(valores)

print("La suma de los valores es:", suma)
print("El promedio de los valores es:", promedio)


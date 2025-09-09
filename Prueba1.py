def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

dato = int(input("Ingrese un número: "))

if 0 <= dato <= 9:
    print("El factorial es:" , factorial(dato))
else:
    print("Solo se permite ingresar un numero de un digito del 0 al 9.")

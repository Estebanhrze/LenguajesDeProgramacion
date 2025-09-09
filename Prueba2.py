class CuentaBancaria:
    
    def __init__(self, nombre , saldo):
        self.nombre = nombre
        self.saldo = saldo
        
    def depositar(self , cantidad):
        self.saldo += cantidad
    
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad
        
    def __str__(self):
        return f"Cuenta bancaria de {self.nombre} con saldo de {self.saldo}"
    
cuenta = CuentaBancaria("Juan Perez",1000)
cuenta.depositar(500)
print(cuenta)
print()

cuenta = CuentaBancaria("Hector Espinoza",2500)
cuenta.depositar(500)
print(cuenta)
cuenta.retirar(50)
print(cuenta)
print()

cuenta = CuentaBancaria("Joseph Carrion",2500)
cuenta.depositar(500)
print(cuenta)
cuenta.retirar(1000)
print(cuenta)
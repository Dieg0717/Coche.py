class CuentaBancaria:
    def __init__(self, titular: str):
        self.titular = titular
        self.saldo = 0.0
    
    def depositar(self, cantidad: float):
        self.saldo += cantidad
        print(f"Depósito de {cantidad} realizado. Saldo actual: {self.saldo} pesos")
    
    def retirar(self, cantidad: float):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado. Saldo actual: {self.saldo} pesos")
        else:
            print("Fondos insuficientes.")
    
    def mostrar_saldo(self):
        print(f"Saldo actual de {self.titular}: {self.saldo} pesos")

if __name__ == "__main__":
    titular = input("Ingrese el nombre del titular de la cuenta: ")
    cuenta = CuentaBancaria(titular)
    
    while True:
        print("\n1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Mostrar saldo")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta.depositar(cantidad)
        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retirar(cantidad)
        elif opcion == "3":
            cuenta.mostrar_saldo()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

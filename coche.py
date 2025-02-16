class Coche:
    def __init__(self, marca: str, modelo: str, color: str):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0
    
    def acelerar(self, velocidad: int):
        self.velocidad += velocidad
        print(f"El coche ha acelerado. Velocidad actual: {self.velocidad} km/h")
    
    def frenar(self, velocidad: int):
        self.velocidad = max(0, self.velocidad - velocidad)
        print(f"El coche ha frenado. Velocidad actual: {self.velocidad} km/h")
    
    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Velocidad: {self.velocidad} km/h")

if __name__ == "__main__":
    coche1 = Coche("Toyota", "Corolla", "Rojo")
    coche1.mostrar_info()
    coche1.acelerar(82)
    coche1.frenar(35)
    coche1.mostrar_info()

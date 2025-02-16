class Rectangulo:
    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho
        self.alto = alto
    
    def calcular_area(self) -> float:
        return self.ancho * self.alto
    
    def calcular_perimetro(self) -> float:
        return 2 * (self.ancho + self.alto)
    
    def mostrar_info(self):
        area = self.calcular_area()
        perimetro = self.calcular_perimetro()
        print(f"Rectángulo - Ancho: {self.ancho}, Alto: {self.alto}, Área: {area}, Perímetro: {perimetro}")

if __name__ == "__main__":
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    alto = float(input("Ingrese la altura del rectángulo: "))
    rectangulo1 = Rectangulo(ancho, alto)
    rectangulo1.mostrar_info()
    
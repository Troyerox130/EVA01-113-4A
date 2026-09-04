class Vehiculo:
    def __init__(self, patente, marca, modelo, año, precio):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def mostrarInfo(self):
        print(f"Patente: {self.patente}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Precio: ${self.precio:,.0f}")

    def calcularAñosUso(self, añoActual):
        if añoActual < self.año:
            return 0
        return añoActual - self.año
class Vendedor:

    def __init__(self, nombre, rut, telefono):
        self.nombre = nombre
        self.rut = rut
        self.telefono = telefono

    def mostrarDatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"RUT: {self.rut}")
        print(f"Teléfono: {self.telefono}")

    def calcularComision(self, montoVenta):
        if montoVenta >= 5000000:
            return montoVenta * 0.10
        return montoVenta * 0.05
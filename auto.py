from vehiculo import Vehiculo


class Auto(Vehiculo):

    def __init__(self, patente, marca, modelo, año, precio,
        numPuertas, combustible):

        super().__init__(patente, marca, modelo, año, precio)

        self.numPuertas = numPuertas
        self.combustible = combustible

    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Número de puertas: {self.numPuertas}")
        print(f"Combustible: {self.combustible}")

    def abrirMaletero(self):
        print("El maletero está abierto.")

    def tieneAireAcondicionado(self):
        return True
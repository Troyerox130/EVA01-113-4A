from vehiculo import Vehiculo


class Motocicleta(Vehiculo):

    def __init__(self, patente, marca, modelo, año, precio, cilindrada, tipo):

        super().__init__(patente, marca, modelo, año, precio)

        self.cilindrada = cilindrada
        self.tipo = tipo

    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Cilindrada: {self.cilindrada} cc")
        print(f"Tipo: {self.tipo}")

    def encenderMotor(self):
        print("La motocicleta está encendida.")

    def esDeAltaCilindrada(self):
        return self.cilindrada >= 500
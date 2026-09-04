from auto import Auto
from motocicleta import Motocicleta
from vendedor import Vendedor
from automotora import Automotora


def main():
    # Crear automotora
    automotora = Automotora("Elden Motors")

    # Crear 2 automóviles
    auto1 = Auto("DS-2748", "Lamborghini", "Murcielago", 2010, 18000000, 4, "Gasolina")
    auto2 = Auto("ER-2587", "Ford", "Mustang", 1998, 22000000, 4, "Diesel")

    # Crear motocicleta
    moto1 = Motocicleta("SK-1879", "Harley-Davidson", "Panhead", 1965, 9500000, 1000, "Chopper")

    # Agregar vehículos a la automotora
    automotora.agregarVehiculo(auto1)
    automotora.agregarVehiculo(auto2)
    automotora.agregarVehiculo(moto1)

    # Mostrar vehículos
    print("===== VEHÍCULOS DE LA AUTOMOTORA =====")
    automotora.mostrarVehiculos()

    # Probar métodos de un Auto
    print("\n===== AUTO =====")
    print(f"Tiene aire acondicionado: {auto1.tieneAireAcondicionado()}")
    auto1.abrirMaletero()

    # Calcular años de uso del auto
    print(f"Años de uso del auto: {auto1.calcularAñosUso(2026)}")
    print(f"Años de uso del auto: {auto2.calcularAñosUso(2026)}")

    # Probar métodos de Motocicleta
    print("\n===== MOTOCICLETA =====")
    print(f"¿Es de alta cilindrada? {moto1.esDeAltaCilindrada()}")
    moto1.encenderMotor()

    # Calcular años de uso de la motocicleta
    print(f"Años de uso de la motocicleta: {moto1.calcularAñosUso(2026)}")

    # Crear vendedor
    vendedor1 = Vendedor("Juan Pérez", "12.345.678-9", "987654321")

    # Mostrar los datos del vendedor
    print("\n===== VENDEDOR =====")
    vendedor1.mostrarDatos()

    # Realizar cálculo de comisión
    monto_venta = 7000000
    comision = vendedor1.calcularComision(monto_venta)

    # Mostrar los resultados obtenidos
    print(f"Monto de venta: ${monto_venta:,.0f}")
    print(f"Comisión: ${comision:,.0f}")


if __name__ == "__main__":
    main()

    #Mi repositorio de git hub es: https://github.com/Troyerox130/EVA01-113-4A.git
#sobre carga de operadores
from sobrecarga_operadores import ViajeroFrecuente


if __name__ == '__main__':
    numero = int(input("Ingrese numero de viajero: "))
    dni = str(input("Ingrese DNI: "))
    nombre = input("Ingrese el Nombre: ")
    apellido = input("Ingrese el apellido: ")
    viajero1 = int(input("Ingrese las millas acumuladas viajero 1: "))
    nuevo = ViajeroFrecuente(numero,dni,nombre,apellido,viajero1)
    viajero2 = int(input("Ingrese las millas acumuladas viajero 2: "))
    otro_viajero = nuevo.__gt__(viajero2)
    if viajero1 > viajero2:
        print("El viajero 1 tiene mas millas que el viajero 2")
    else:
        print("El viajero 2 tiene mas millas que el viajero 1")
    val = nuevo.__rad__(viajero2)
    print(f"millas acumuladas >> {val}")
    aux = int(input("Ingrese las millas ah canjear: "))
    print(f"Canjeo de millas exitoso! millas restantes >> {nuevo.__rsub__(aux)}")
    equivalente = nuevo.__req__(viajero2)
    print(f"La cantidad de millas son equivalentes --> {equivalente}")
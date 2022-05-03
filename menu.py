def MuestraMenu():
    __op=0
    while True:
        print("----------Eliga una opcion----------\n")
        print("1. Actualizar el valor del vehiculo de cada plan.\n")
        print("2. Ingrese un valor para ver datos de las cuotas menores a el.\n")
        print("3. Mostrar monto que se debe haber pagado para licitar el vehiculo.\n")
        print("4. Dado el codigo de un plan, modificar la cantidad de cuotas que debe tener pagas para licitar\n")
        print("5.salir\n")
        __op=input("Ingrese su opcion: ")
        if __op in ("1", "2", "3","4","5"):
            return __op
        input(("No se ha ingresado ninguna opcion correcta.\n""Pulsa ENTER para continuar\n"))

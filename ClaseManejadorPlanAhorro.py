import csv
from ClasePlanAhorro import PlanAhorro
class ManejadorPlanAhorro:
    def __init__(self):
        self.__ListaPlanes=[]

    def __str__(self):
        s = ""
        for plan in self.__ListaPlanes:
            s += str(plan) + '\n'
        return s

    def agregarPlan(self,unPlan):
        self.__ListaPlanes.append(unPlan)

    def CrearPlan(self):
        with open("planes.csv","r") as file:
                reader=csv.reader(file,delimiter=";")
                for fila in reader:
                    codPlan = int(fila[0])
                    modelo = fila[1]
                    version = fila[2]
                    valor = int(fila[3])
                    cantCuotas = int(fila[4])
                    cantCuotasLicitar = int(fila[5])
                    unPlan = PlanAhorro(codPlan,modelo,version,valor)
                    self.agregarPlan(unPlan)

    def actualizarValor(self):
        for cod, PlanAhorro in enumerate (self.__ListaPlanes):
            print("Codigo del plan: {}, Modelo: {}, Version del modelo: {}\n".format(PlanAhorro.getCodigo(),PlanAhorro.getModelo(),PlanAhorro.getVersion()))
            valorActual=int(input("Ingrese valor actual del vehiculo: "))
            if PlanAhorro.getValor() == valorActual:
                aux2=int(input("Ingrese nuevo valor: "))
                PlanAhorro.setValor(aux2)
                print("El valor fue actualizado.\n")
            else: print("Valor Incorrecto")

    def SegunValor(self):
        aux=int(input("Ingrese un valor para consultar: \n"))
        for cod, PlanAhorro in enumerate (self.__ListaPlanes):
            valorCuota= int(((PlanAhorro.getValor()/PlanAhorro.getCantCuotas()) + PlanAhorro.getValor()*0.10))
            print("Valor cuota: {}".format(valorCuota))
            if (valorCuota < aux):
                print("Codigo del plan: {}, Modelo: {}, Version del modelo: {}\n".format(PlanAhorro.getCodigo(),PlanAhorro.getModelo(),PlanAhorro.getVersion()))
            else: print("No hay cuotas menores a ese valor")

        '''  
        valorCuota.append(int(((PlanAhorro.getValor()/PlanAhorro.getCantCuotas()) + PlanAhorro.getValor()*0.10)))
        for i in range (len(valorCuota)):
            print("Valor cuota: {} del plan: {} ".format(valorCuota[i],i+1))
            for cod, PlanAhorro in enumerate (self.__ListaPlanes):
                if (valorCuota[i] < aux):
                    print("Codigo del plan: {}, Modelo: {}, Version del modelo: {}\n".format(PlanAhorro.getCodigo(),PlanAhorro.getModelo(),PlanAhorro.getVersion()))
                else: print("No hay cuotas menores a ese valor") '''

    def MontoLicitar(self):
        for cod, PlanAhorro in enumerate (self.__ListaPlanes):
            valorCuota= int(((PlanAhorro.getValor()/PlanAhorro.getCantCuotas()) + PlanAhorro.getValor()*0.10))
            print(f"El monto que se debe haber pagado para licitar el vehiculo del plan con codigo: {PlanAhorro.getCodigo()} es: {PlanAhorro.getCantCuotas()*valorCuota}")

    def ModificarCuotasLicitar(self):
        aux=int(input("Ingrese codigo de plan: \n\n"))
        for cod, PlanAhorro in enumerate (self.__ListaPlanes):
            if PlanAhorro.getCodigo()==aux:
                cant=int(input("Ingrese la nueva cantidad de cuotas para licitar: \n"))
                PlanAhorro.setCuotasLicitar(cant)
                print("La cantidad se modifico correctamente\n")

import sys
from ClaseManejadorPlanAhorro import ManejadorPlanAhorro
from menu import MuestraMenu
if __name__=="__main__":

    mp = ManejadorPlanAhorro()
    mp.CrearPlan()
    print('Planes: \n')
    print(mp)
    while True:
        op = MuestraMenu()
        if op == '1':
            mp.actualizarValor()
        elif op == '2':
            mp.SegunValor()
        elif op == '3':
            mp.MontoLicitar()
        elif op == '4':
            mp.ModificarCuotasLicitar()
        elif op == '5':
            sys.exit(0)

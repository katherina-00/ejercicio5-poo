class PlanAhorro:
    # atributos de clase:
    __cantCoutas=int(60)
    __cantCuotasLicitar=int(10)


    def __init__(self,codPlan,modelo,version,valor):
        self.__codPlan = codPlan
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor

    def __str__(self):
        return "%d %s %s %d %d %d" % (self.__codPlan, self.__modelo, self.__version, self.__valor, self.__cantCoutas, self.__cantCuotasLicitar)

    def getCodigo(self):
        return self.__codPlan
    def getModelo(self):
        return self.__modelo
    def getVersion(self):
        return self.__version
    def getValor(self):
        return self.__valor
    def setValor(self,nuevoValor):
        self.__valor=nuevoValor
    #metodos de clase
    @classmethod
    def getCantCuotas(cls):
        return cls.__cantCoutas
    @classmethod
    def getCantCuotasLicitar(cls):
        return cls.__cantCuotasLicitar
    @classmethod
    def setCuotasLicitar(cls,nuevoValor):
        cls.__cantCuotasLicitar=nuevoValor

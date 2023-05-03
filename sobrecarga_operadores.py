#Defino clase Viajeros Frecuentes

class ViajeroFrecuente:
    __numero: int
    __dni: str
    __nombre: str
    __apellido: str
    __acum_millas: int
   
    #Definicion del constructor
    
    def __init__(self,num,dni,nom,ape,acum_millas):
        self.__numero = num
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = ape
        self.__acum_millas = acum_millas
    def getdatos(self):
        return print(f"Bienvenido viajero numero: {self.__numero} | DNI Ingresado: {self.__dni} | Estimado: {self.__nombre}{self.__apellido} | Tiene acumulado un total de {self.__acum_millas} millas")
    
    def __gt__(self,otro_viajero: int):
        return self.__acum_millas > otro_viajero
    def __rad__(self,v):
        v = 100 + v
        return v
    def __rsub__(self,v):
        v = 100 - v
        return v
    def __req__(self,v):
        return 100 == v
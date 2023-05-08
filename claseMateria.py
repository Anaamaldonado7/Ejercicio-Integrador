class Materia:
    __dni = 0
    __nombreM = ''
    __fecha = ''
    __nota = 0
    __aprobacion = ''
    
    def __init__(self, dni, nombreM, fecha, nota, aprobacion):
        self.__dni = dni
        self.__nombreM = nombreM
        self.__fecha = fecha
        self.__nota= nota
        self.__aprobacion = aprobacion
        
    def getDNI(self):
        return self.__dni
    def getMateria(self):
        return self.__nombreM
    def getFecha(self):
        return self.__fecha
    def getNota(self):
        return self.__nota
    def getAprobacion(self):
        return self.__aprobacion
class Alumno:
    __dni=''
    __apellido=''
    __nombre=''
    __carrera=''
    __anio=0
    
    def __init__(self, dni, apellido, nombre, carrera, anio):
        self.__dni = dni 
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__anio = anio
        
    def getDni(self):
        return self.__dni
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getCarrera(self):
        return self.__carrera
    def getAnioCarrera(self):
        return self.__anio
    def __lt__(self, name):
        return self.getAnioCarrera() < name.getAnioCarrera()

import numpy as np 
from claseAlumno import Alumno 
import csv 
class manejadorAlumno:
    __cantidad = 0 
    __dimension = 0
    __incremento = 5 
    
    def __init__ (self, dimension = 5, incremento = 5): 
       self.__alumnos = np.empty(dimension, dtype=Alumno)
       self.__cantidad = 0
       self.__dimension = dimension 
       self.__incremento = incremento 
       
    def agregar (self, alu):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__alumnos.resize(self.__dimension)
        self.__alumnos[self.__cantidad] = alu
        self.__cantidad += 1  
        
    def CargaArreglo(self):
        archivo = open('alumnos.csv')
        reader = csv.reader(archivo, delimiter = ';')
        for fila in reader:
            alu=Alumno(fila[0], fila[1] , fila[2], fila[3], fila[4]);
            self.agregar(alu)    
            
    def mostrar(self):
       for i in range(len(self.__alumnos)):   
           print("DNI: {} ".format(self.__alumnos[i].getDni()))

    def listar (self):
        lista = self.__alum.tolist()
        lista.sort()
        for alum in lista:
            print("{} {} Año que cursa: {}".format(alum.getapellido()))
    def getAlum(self, dni):
        i=0
        flag = False
        alum = None
        while i<=len(self.__alum) and flag == False:
            if self.__alum[i].getDni()==str(dni):
                flag = True
                alum = self.__alum[i]
                i+=1
        return(alum)
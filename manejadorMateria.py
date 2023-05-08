import numpy as np
import csv
from claseMateria import Materia
from manejadorAlumno import manejadorAlumno
import math

class manejadorMateria:
    __listaMaterias = []
    def __init__(self):
        self.__listaMaterias = []
    def Carga(self):
        archivo = open("materiasAprobadas.csv")
        reader = csv.reader(archivo,delimiter=";")
        for fila in reader:
            a = Materia(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__listaMaterias.append(a)
        archivo.close()

def promedio (self):
     prom_Aplazos = 0
     prom_SinAplazos = 0
     conta = 0
     contS=0
     dni = input("Ingrese DNI del alumno: ")
     for i in range(len(self.__listaMaterias)):
            if (dni == self.__listaMaterias[i].getDNI()):
                if (self.__listaMaterias[i].getnota() >= 7):
                    prom_SinAplazos += self.__listaMaterias[i].getnota()
                    contS += 1
                prom_Aplazos += self.__listaMaterias[i].getnota()
                conta +=1
     notaAp = (prom_Aplazos/conta)
     notasap = (prom_SinAplazos/contS)
     print("Promedio con aplazos: ", notaAp)
     print("Promedio sin aplazos: ", notasap)

def promociones(self):
         b=manejadorAlumno(10)
         b.CargaArreglo()
         nombre = input("Ingrese nombre de materia: ")
         for i in range (len(self.__listaMaterias)):
             if (self.__listaMaterias[i].getnombreM() == nombre):
              if (self.__listaMaterias[i].getaprobacion() == 'P'):
                     print(f"{self.__listaMaterias[i].getDni() : <20}")
                     print(f"{b.getAlum(self.__listaMaterias[i].getDNI()).getAlum() : <30}")
                     print(f"{self.__listaMaterias[i].getfecha() : <15}")
                     print(f"{self.__listaMaterias[i].getnota() : < 4}")
                     print(f"{b.getAlum(self.__listaMaterias[i].getdni()).getcursado}")

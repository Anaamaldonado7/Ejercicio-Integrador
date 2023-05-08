from manejadorAlumno import manejadorAlumno
from manejadorMateria import manejadorMateria

class menu:
    opcion = 0
    
    def MenuOpciones(self):
        alu = manejadorAlumno(10)
        mat = manejadorMateria()
        alu.CargaArreglo()
        mat.Carga()
        print("--MENU OPCIONES--")
        print("1. Informar promedio de alumno con aplazos y sin aplazos mediante DNI")
        print ("\n2.Informar estudiantes que aprobaron materia ingresada por teclado")
        print("\n3.Obtener Listado ordenado de alumnos")
        self.__opcion = input("\nSeleccione una opcion: ")
        if self.__opcion == "1":
            mat.promedio()
        elif self.__opcion == "2":
            mat.promociones()
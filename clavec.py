import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 2 numeros
2*4 = 8
"""


# start-->
def multiplicar(numero1, numero2):
    return numero1*numero2


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1 al 1000
"""


# start-->
def sumaDivTresYCinco(num1, num2):
    result = sum([i for i in range(num1, num2 +1) if i % 3 == 0 or i % 5 == 0])
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el generatriz, area y el volumen de un cono
radio = 5 m
altura = 11 m

generatriz: square_root(altura^2 + radio^2)
area: pi*radio*(radio+generatriz)
volumen: (1/3)*pi*radio^2*altura
"""


# start-->
def definicionCono(self,radio, altura):
    diccionario = {"generatriz:": obtenerGeneratriz, "area:":obtenerArea, "volumen:":obtenerVolumen}
    result= diccionario

      
    return result


def obtenerGeneratriz(radio1, altura1):
     gene = sum(altura1*altura1 + radio1*radio1)
     generatriz = math.sqrt(gene)
    
     return generatriz


def obtenerArea():
    result = math.pi*radio2*(radio2+obtenerGeneratriz(5,11))
     
    return result


def obtenerVolumen(radio3, altura3):
    result = 1/3*math.pi*(radio3*radio3)*altura3
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Cono:
     def __init__(self, radio, altura, volumen):
         self.__radio = radio
         self.__altura = altura
         self.__volumen = volumen

     def definicionCono(self, radio, altura,volumen):
        result = obtenerGeneratriz(5,11), obtenerArea(5,11), obtenerVolumen(5,11)
        return result

        


"""
***************************************************************
@@ ejercicio 5 @@
CentroMedico
Paciente
    nombre
    lugar
    descripcion
    costo
    conDescuento
    descuento
"""


class CentroMedico:
    def __init__(self, Nombre, Lugar, Descripcion, Costo, Descuento):
     self.__Nombre = Nombre
     self.__Lugar= Lugar
     self.__Descripcion = Descripcion
     self.__Costo = Costo
     self.__Descuento= Descuento
    



"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return ""
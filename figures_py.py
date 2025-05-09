# -*- coding: utf-8 -*-
"""Figures.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12fYvpfnOTG2TrspWR7oa4GlbdkY4UkF7
"""

import math


class Figura:

    def __init__(self,nombre):
        self.nombre = nombre
        self.area = None
        self.perimetro = None

    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

    def mostrarInfo(self):
        self.calcular_area()
        self.calcular_area()
        print(f"Nombre de la figura {self.nombre}")
        print(f"Área de la figura {self.area}")
        print(f"Perímetro de la figura {self.perimetro}")

class Circulo(Figura):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2


    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
class Rectangulo(Figura):
    def __init__(self, longitud, base):
        self.longitud = longitud
        self.base = base

    def calcular_area(self):
        return self.longitud * self.base

    def calcular_perimetro(self):
        return 2 * (self.longitud + self.base)

class Triangulo(Figura):

    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_area(self):
        return 0.5 * self.base * self.altura

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

import Figures
from Figures import *

fig_1=Figura("circulo")
circulo= Circulo("circulo",2)
circulo

circulo.calcular_area()

fig_2=Figura("triangulo")
triangulo= Triangulo("triangulo", 2,3,4,2)
triangulo.calcular
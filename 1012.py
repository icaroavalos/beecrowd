# -*- coding: utf-8 -*-

# Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
# a) a área do triângulo retângulo que tem A por base e C por altura.
# b) a área do círculo de raio C. (pi = 3.14159)
# c) a área do trapézio que tem A e B por bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B.

abc = input().split()
a = float(abc[0])
b = float(abc[1])
c = float(abc[2])

triangulo = ((a*c)/2)
circulo = (3.14159*c*c)
trapezio = (((a+b)*c)/2)
quadrado = (b*b)
retangulo = (a*b)

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")
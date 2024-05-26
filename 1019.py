# -*- coding: utf-8 -*-

# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma 
# fábrica, e informe-o expresso no formato horas:minutos:segundos.

n = int(input())

horas = n//3600

t = n%3600
minutos = t//60

segundos = n%60

print(f'{horas}:{minutos}:{segundos}')
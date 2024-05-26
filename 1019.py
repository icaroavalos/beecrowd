# -*- coding: utf-8 -*-

n = int(input())


horas = n//3600

t = n%3600
minutos = t//60

segundos = n%60

print(f'{horas}:{minutos}:{segundos}')
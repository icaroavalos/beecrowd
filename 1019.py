# -*- coding: utf-8 -*-

n = int(input())

horas = n//3600
t =n%3600
minutos = n//60
n = n-n//60

print(f'{t}')
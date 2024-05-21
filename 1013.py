# -*- coding: utf-8 -*-

#Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.

abc = input().split()
a = int(abc[0])
b = int(abc[1])
c = int(abc[2])

maior1 = (a+b+abs(a-b))/2
maior2 = (maior1+c+abs(maior1-c))/2

print(f'{maior2:.0f} eh o maior')
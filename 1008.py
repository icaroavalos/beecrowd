# -*- coding: utf-8 -*-

# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que 
# recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, 
# com duas casas decimais.

num_func = int(input())
hrs_trab = int(input())
valor_hora = float(input())

salario = hrs_trab*valor_hora

print(f'NUMBER = {num_func}')
print(f'SALARY = U$ {salario:.2f}')
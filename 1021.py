# -*- coding: utf-8 -*-

valor = float(input())

notas = [100, 50, 20, 10, 5, 2]

print('NOTAS:')
for i in notas:
    print(f'{valor//i:.0f} nota(s) de R$ {i:.2f}')
    valor = valor%i
    
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
    
print('MOEDAS:')
for i in moedas:
    print(f'{valor//i:.0f} moedas(s) de R$ {i:.2f}')
    valor = valor%i
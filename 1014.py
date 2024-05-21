# -*- coding: utf-8 -*-

# Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).

km = int(input())
litro = float(input())

media = km/litro

print(f'{media:.3f} km/l')
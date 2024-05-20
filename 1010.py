# -*- coding: utf-8 -*-

# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código 
# de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

peça1 = input().split()
codpeça1 = int(peça1[0])
numpeça1 = int(peça1[1])
valorunidade1 = float(peça1[2])

peça2 = input().split()
codpeça2 = int(peça2[0])
numpeça2 = int(peça2[1])
valorunidade2 = float(peça2[2])

valor_pagar = ((numpeça1*valorunidade1)+(numpeça2*valorunidade2))

print(f"VALOR A PAGAR: R$ {valor_pagar:.2f}")
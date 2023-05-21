#!/usr/bin/env python3
from polka.tools import calculate_routeid, print_poly, generate_nodeids
DEBUG=False

mindegree = 3
n = 5

sondas = [[3, 1, 0, 2, 4, 8], [10, 9], [7], [5, 11, 18], [12, 14, 15, 16, 17], [13], [6]]
o = []
for sonda in sondas:
    estado_sonda = []
    for i in range(len(sonda)):
        estado_switch = [0] * len(sonda)
        if i < len(sonda) - 1:
            estado_switch[i+1] = 1  # Ativar a porta para o próximo switch na sonda
        estado_sonda.append(estado_switch)
    o.append(estado_sonda)

print(o)

node_ids = generate_nodeids(mindegree, n)
print(node_ids)

'''
Input Format:

The first line of input contains space separated values of N and M.
The next N lines contains M space separated integers.

Output Format:

Compute the sum along axis 0. Then, print the product of that sum.'''

import numpy as np
line = [int(x) for x in input().split()]
lista = []
for x in range(line[0]):
    lista_inteiro = [int(x) for x in input().split()]
    lista.append(lista_inteiro)
print(np.prod(np.sum(np.array(lista), axis = 0)))
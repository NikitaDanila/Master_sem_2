nr = []
import itertools
n = input('Nr trepte= ')

nr.insert(0,1)
nr.insert(1,2)

for i,j in zip(nr[2:], nr[3:]):
    nr.append(i-1 + j-2)

print(f'{nr[-1]} modalitati de urcare pe scara cu {n} trepte')
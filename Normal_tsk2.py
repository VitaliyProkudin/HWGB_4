import random
import pprint

line = 4
row_u = 4
matr = []
for i in range(line):
    row = []
    row_zero = [random.randint(0, row_u) for x in range(row_u)]
    for m in range(row_u):
        if row_zero[i] == m:
            row.append(0)
        else:
            row.append(random.randint(1, 100))
    matr.append(row)
#if Don't' job pprint
# for i in matr:
#     print(i)
pprint.pprint(matr)
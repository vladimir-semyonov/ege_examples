'''
Определите количество девятеричных пятизначных чисел, в записи которых
ровно одна цифра 0, при этом никакая нечётная цифра не стоит рядом с цифрой 0.
'''
from itertools import product
s = '012345678'
res = set()
for x in product(s, repeat=5):
    a = ''.join(x)
    if a[0] != '0' and a.count('0') == 1 and sum('0' + c in a or c + '0' in a for c in '1357') == 0:
        res.add(a)
print(len(res))

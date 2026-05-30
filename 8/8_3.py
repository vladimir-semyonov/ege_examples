'''
Определите количество 15-ричных пятизначных чисел, в записи которых 
ровно одна цифра 8 и не менее двух цифр с числовым значением, превышающим 9.
'''
from itertools import product
s = [c for c in range(15)]
res = 0

for x in product(s, repeat=5):
    if x[0] != 0 and x.count(8) == 1 and sum(c > 9 for c in x) >= 2:
        res+=1
print(res)

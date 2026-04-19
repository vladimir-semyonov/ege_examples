#использует @lru_cache для кеширования больших значений
from functools import *
@lru_cache(None) 

#программируем функцию по условию
def f(n):
    if n <= 10:
        return n 
    if n > 10:
        return n - 7 + f(n-21)

#кэшируем значения
for i in range(10, 200000):
    f(i)

#выводим ответ по условию
print((f(185734) - f(185650))/f(40))

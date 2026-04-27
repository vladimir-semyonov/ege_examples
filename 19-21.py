from functools import *

def step(p):
    return p + 1, p * 3

def win(p):
    return p <= 116

@lru_cache(None)
def game(p):
    if win(p): return 0
    if any(game(p1) == 0 for p1 in step(p)): return 1
    if all(game(p1) == 1 for p1 in step(p)): return 2
    if any(game(p1) == 2 for p1 in step(p)): return 3
    if all(game(p1) in (1, 3) for p1 in step(p)): return 4

for s in range(117, 10000):
    if game(s) == 4:
        print(s, end=' ')

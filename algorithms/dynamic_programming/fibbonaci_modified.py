from functools import lru_cache

line_input = input()
t1, t2, term = map(int, line_input.split(" "))

@lru_cache(maxsize=32)
def fibonnaci(n):
    if n == 1:
        return t1
    elif n == 2:
        return t2
    else:
        return fibonnaci(n-2) + fibonnaci(n-1) ** 2

print (fibonnaci(term))

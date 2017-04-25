from functools import cmp_to_key

def cmp(x, y):
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)

    if x == y:
        return 0
    elif x < y:
        return -1
    else:
        return 1

n = int(input())
print("\n".join(sorted([input() for _ in range(n)], key=cmp_to_key(cmp))))

#source https://www.hackerrank.com/challenges/sherlock-and-array
from itertools import accumulate

T = int(input())

for _ in range(T):
    n = int(input())
    a = [int(x) for x in input().split(" ")]

    a_cumsum = list(accumulate(a))
    rev_cumsum = list(accumulate(a[::-1]))

    #Special case
    found = len(a) == 1

    i = 1
    while i < n - 1 and not found:
        if a_cumsum[i - 1] == rev_cumsum[n - i - 2]:
            found = True
        i += 1

    if found:
        print("YES")
    else:
        print("NO")



"""
Another way to solve the problem using dicts

for _ in range(T):
    n = int(input())
    a = [int(x) for x in input().split(" ")]

    a_cumsum = list(accumulate(a))

    rev_cumsum = {cumsum: x for x, cumsum in enumerate(accumulate(a[::-1]))}

    found = False
    for i, cumsum in enumerate(a_cumsum):
        rev_i = rev_cumsum.get(cumsum, -1)

        if rev_i + 1 + i == n:
            found = True
            break

    if found:
        print("YES")
    else:
        print("NO")
"""

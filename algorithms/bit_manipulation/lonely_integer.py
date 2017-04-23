#source https://www.hackerrank.com/challenges/lonely-integer
from functools import reduce

N = int(input())
print (reduce(int.__xor__, list(map(int, input().split(" ")))))

"""
properties:
    - commutative
        a ^ b = b ^ a

    - Asociative
        (a ^ b) ^ c = a ^ (b ^ c)

    - Neutral element
        a ^ 0 = a

    - Xor inverse property
        a ^ b = 0 (if a = b)
"""

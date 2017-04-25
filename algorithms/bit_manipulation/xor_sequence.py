#source https://www.hackerrank.com/challenges/xor-se
T = int(input())

queries = [list(map(int, input().split(" "))) for _ in range(T)]

def calculate(fr, to, row):
    res = 0

    for i in range(fr, to + 1):
        if i == 0:
            res ^= (4 * row)
        elif i == 1:
            res ^= 1
        elif i == 2:
            res ^= (4 * row + 3)

    return res

for l, u in queries:
    l_value = l % 4
    l_row = l // 4

    u_value = u % 4
    u_row = u // 4

    """
    A even number of rows between them doesn't do anything
    because a1^a2^a3^a4..^an = 0 (Where n is even)

    If the number of rows between them is odd, their xor is 2.

    (Xor associativity, Xor inverse of a number is itself)
    """
    middle_rows_xor =  2 * ((u_row - l_row + 1) % 2)

    print(calculate(l_value, 3, l_row) ^ calculate(0, u_value, u_row) ^ middle_rows_xor)

"""

2


[ 0, 1, 3, 0,  => 0 ^ 1 ^ 3 ^ 0  = 2
  4, 1, 7, 0,  => 4 ^ 1 ^ 7 ^ 0  = 2
  8, 1, 11, 0, ..
 12, 1, 15, 0, ..
 16, 1, 19, 0, ..
 20, 1, 23, 0, ..
 24, 1, 27, 0, => 24 ^ 1 ^ 27 ^ 0 = 2
 28, 1, 31, 0]

"""

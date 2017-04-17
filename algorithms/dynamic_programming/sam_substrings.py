#source https://www.hackerrank.com/challenges/sam-and-substrings
number = [int(x) for x in input()]
modulus = 10 ** 9 + 7
len_number = len(number)

acc = 0
res = 0

for i in range(0, len(number)):
    acc = (10 * acc + 1) % modulus
    wrap_num = len_number - i
    res = (res + wrap_num * acc * number[wrap_num - 1]) % modulus

print (res)
"""
x y z u


x -> 1 time as x
  -> 1 time as 10x
  -> 1 time as 100x
  -> 1 time as 1000x

y -> 2 times as y
  -> 2 times as y0
  -> 2 times as y00

z -> 3 times as z
z -> 3 times as z0

w -> 4 times as w

Ex:
123 are 1, 2, 3, 12, 23, 123

= 1 * (1 * 111) + 2 * (2 * 11) + 3 * (3 * 1)
= 111 + 44 + 9 = 164

"""

#source  https://www.hackerrank.com/challenges/maximizing-xor

l = int(input())
u = int(input())

value = l ^ u
# msb (value) = (1 << len(bin(value)) - 2)
result = (1 << len(bin(value)) - 2) - 1
print(result)

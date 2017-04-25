#source https://www.hackerrank.com/challenges/sum-vs-xor
n = int(input())
#Bin function represents 0 as 0b0, which would yield 2 solutions instead  1
#so we have to add an expectial case, the number of zeros when n=0 should be 0.
zeros = bin(n).count('0') - 1 if n > 0 else 0

print(1 << zeros)

#source https://www.hackerrank.com/challenges/missing-numbers
from collections import Counter

N = int(input())
a_freqs = Counter([int(x) for x in input().split(" ")])

M = int(input())
b_freqs = Counter([int(x) for x in input().split(" ")])

missing_numbers = []

for number, frequency in b_freqs.items():
    frequency_a = a_freqs.get(number, 0)

    if frequency_a != frequency:
        missing_numbers.append(number)

print (" ".join([str(x) for x in sorted(missing_numbers)]))

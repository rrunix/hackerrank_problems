#source https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array
import sys
import bisect

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

a = sorted(a)
min_abs = abs(a[0] - a[1])

for i in range(1, n - 1):
    test_abs = abs(a[i] - a[i + 1])

    if test_abs < min_abs:
        min_abs = test_abs

print (min_abs)

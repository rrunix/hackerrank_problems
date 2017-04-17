#Source https://www.hackerrank.com/challenges/marcs-cakewalk
import sys

n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))
print (sum((1 << i) * c for i, c in enumerate(reversed(sorted(calories)))))

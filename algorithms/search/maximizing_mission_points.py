import bisect

import sys
sys.stdin = open("input.in", "r")

n, x, y = map(int, input().split(" "))
cities = [tuple(map(int, input().split(" "))) for _ in range(n)]

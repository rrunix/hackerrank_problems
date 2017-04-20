#source https://www.hackerrank.com/challenges/knightl-on-chessboard
from collections import defaultdict

N = int(input())
for _ in range(N):
    m = int(input())
    n = int(input())

    costs = defaultdict(list)
    for i, cost in enumerate(input().split(" ")):
        cost = int(cost)
        if cost < m:
            costs[cost].append(i)

    idx_i = 0
    idx_j = 0

    for cost, i in costs.items():

        if cost * 2 == m:
            idx_i = i[0] + 1
            idx_j = i[1] + 1
            break

        elif  (m - cost) in costs:
            idx_i = i[0] + 1
            idx_j = costs[m - cost][0] + 1
            break

    print (min(idx_i, idx_j), max(idx_i, idx_j))

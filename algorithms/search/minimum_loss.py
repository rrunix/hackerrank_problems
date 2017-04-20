#source https://www.hackerrank.com/challenges/minimum-loss
import math

N = int(input())
prices = list([int(x) for x in input().split(" ")])

prices = sorted(enumerate(prices), key=lambda x: x[1], reverse=True)

#Max possible loss
minimum_loss = math.pow(10, 16)

for i in range (N):
    year, price = prices[i]

    j = i + 1
    while j < N and prices[j][0] < year:
        j += 1

    if j < N:
        minimum_loss = min(minimum_loss, prices[i][1] - prices[j][1])

print (minimum_loss)

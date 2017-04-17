#https://www.hackerrank.com/challenges/candies
N = int(input())

ratings = [0] * N
candies = [1] * N

ratings[0] = int(input())

for i in range(1, N):
    rating = int(input())
    ratings[i] = rating

    if ratings[i - 1] < ratings[i]:
        candies[i] = candies[i - 1] + 1

for i in range(N - 1, 0, -1):
    if ratings[i - 1] > ratings[i] and candies[i - 1] <= candies[i]:
        candies[i - 1] = candies[i] + 1

print(sum(candies))

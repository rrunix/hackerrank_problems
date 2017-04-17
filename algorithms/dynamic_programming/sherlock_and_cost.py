#source https://www.hackerrank.com/challenges/sherlock-and-cost

def calculateAs(Bs):
    As = list(Bs)
    print (Bs)
    leftAs = [0] * len(Bs)
    rightAs = [0] * len(Bs)


    for i in range(0, len(As) - 1):
        if Bs[i + 1] > Bs[i]:
            leftAs[i + 1] = 1
        else:
            leftAs[i + 1] = 0

    for i in range(1, len(As)):
        if Bs[i] < Bs[i - 1]:
            rightAs[i - 1] = 1
        else:
            rightAs[i - 1] = 0


    print (leftAs)
    print (rightAs)

def calculateS(As):
    score = 0
    for i in range(1, len(As)):
        score += abs(As[i] - As[i - 1])

    return score

"""
import sys
sys.stdin = open("input.in", "r")

T = int(input())
for _ in range(T):
    N = int(input())
    Bs = [int(x) for x in input().split(" ")]

    print (calculateAs(Bs))

"""
max_score = [1, 1, 1, 1]
score = calculateS(max_score)

for i in range(1, 9):
    for j in range(1, 10):
        for z in range(1, 9):
            for w in range(1, 2):
                test = [i, j, z, w]
                test_score = calculateS(test)

                if test_score > score:
                    max_score = test
                    score = test_score

print (max_score, score)

"""
Bs: 10 1 10 1 10
As: 10 1 10 1 10 => 9 + 9 + 9 + 9 = 36


Bs: 10 10 10 10
As: 10 1 10 1 => 9 + 9 + 9 = 27

Bs: 8 9 8 1
As: 8 1 8 1

    0 2 1
      1 0 0

    -1 1 7

    Bs[i] = Bs[i] - Bs[i + 1]


=
    0 3 1 0

Bs: 8 9 8 9
As: 1 9 1 9



"""

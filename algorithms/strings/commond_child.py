#source https://www.hackerrank.com/challenges/common-child
#used pypy3 to pass the tests, python 3 timeouts.

seq1 = input()
seq2 = input()

seq1_l = len(seq1)
seq2_l = len(seq2)

dp = [[0]*(seq1_l + 1) for i in range(seq2_l + 1)]

for i in range(0, seq1_l):
    for j in range(0, seq2_l):
        if(seq1[i]==seq2[j]):
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

print(dp[-1][-1])

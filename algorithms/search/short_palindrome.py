#source https://www.hackerrank.com/challenges/short-palindrome

MOD=10**9+7
letter_floor = ord('a')

letters=[ord(x) - letter_floor for x in input()]
n=len(letters)

#Initialize first iteration outside the loop, so we don't need to include
#a condition in the loop
frequencies = []
frequencies.append([0] * 26)
frequencies[0][letters[0]]+=1

#Frequencies until position i
for i in range(1, n):
    frequencies.append(list(frequencies[-1]))
    frequencies[i][letters[i]]+=1

suffixes = [[0 for x in range(26)] for y in range(26)]

#Given that we known that letters[i] has appear, what's the number of times
#that j has appear from i to the final.
for i in range(1, n):
    for j in range(26):
        suffixes[letters[i]][j] += (frequencies[-1][j] - frequencies[i][j])

sol = 0
for i in range(1, n-2):

    #Palindrome with letters[i] and j.
    #Which is calculated as the times that j has appear on iteration i multiplied
    #by the times that letters[i] has appear before j
    for j in range(26):
        suffixes[letters[i]][j] -= (frequencies[-1][j] - frequencies[i][j])
        sol = (sol + (frequencies[i-1][j] % MOD) * (suffixes[letters[i]][j] % MOD)) % MOD
    #JIIJ

print (sol)

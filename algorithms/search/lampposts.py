import sys

N, M, K = map(int, input().split(" "))
lampposts = M * N

tracks = sorted([[int(x) for x in line.split(" ")] for line in sys.stdin])

i = 0
while i < K:
    row, c1, c2 = tracks[i]
    lampposts -= c2 - c1 + 1

    i += 1
    while i < K and tracks[i][0] == row:
        _, c1c, c2c = tracks[i]

        if c1c <= c2:
            c1c = c2 + 1

        if c1c <= c2c:
            lampposts -= c2c - c1c + 1
            c2 = c2c

        i += 1

print (lampposts)

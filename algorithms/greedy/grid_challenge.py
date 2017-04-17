#source https://www.hackerrank.com/challenges/grid-challenge

def are_columns_sorted(grid):
    for i in range(N):
        for j in range(N - 1):
            if grid[j][i] > grid[j + 1][i]:
                return False
    return True

T = int(input())
for _ in range(T):
    N = int(input())
    grid = [sorted(list(input())) for _ in range(N)]

    print("YES" if are_columns_sorted(grid) else "NO")

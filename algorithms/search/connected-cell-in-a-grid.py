#source https://www.hackerrank.com/challenges/connected-cell-in-a-grid

def dfs(pos, grid):
    area = 0
    if pos in grid:
        area += 1
        grid.remove(pos)
        for mov in movements:
            area += dfs((pos[0] - mov[0], pos[1] - mov[1]), grid)

    return area

n = int(input())
m = int(input())

grid = set()
movements = [(1, 1), (-1, 1), (-1, -1), (1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(n):
    line = [x == "1" for x in input().split(" ")]
    for j in range(m):
        if line[j]:
            grid.add((i, j))

max_area = 0
while len(grid) > 0:
    element = next(iter(grid))
    max_area = max(max_area, dfs(element, grid))

print (max_area)

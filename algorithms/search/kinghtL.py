#source https://www.hackerrank.com/challenges/knightl-on-chessboard

def bfs(x, y, target_x, target_y, movements):
    stack = list()
    stack.append((x, y, 0))
    to_visit = set()

    if x == target_x and y == target_y:
        return 0
    else:
        i = 0
        while len(stack) > 0:
            x, y, depth = stack.pop(0)

            for dx, dy in movements:
                px = x + dx
                py = y + dy

                if px == target_x and py == target_y:
                    return depth + 1
                elif (0 <= px < N and 0 <= py < N) and not ((px, py) in to_visit):
                        stack.append((px, py, depth + 1))
                        to_visit.add((px, py))
            i += 1

    return -1

N = int(input())

for i in range(1, N):
    for j in range(1, N):
        cache = dict()
        movements = [(i, j), (i, -j), (-i, -j), (-i, j),
                     (j, i), (j, -i), (-j, -i), (-j, i)]
        distance = bfs(0, 0, N - 1, N - 1, movements)
        print (distance, end=" ")
    print("")

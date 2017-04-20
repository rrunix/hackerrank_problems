N, K = map(int, input().split(" "))
houses = sorted([int(x) for x in input().split(" ")])

i = 0
num_transmitters = 0

while (i < N):
    left_pivot = houses[i]
    last_i = i

    while (i < N and houses[i] <= left_pivot + K):
        i += 1

    tower_pos = i - 1
    while (i < N and houses[i] <= houses[tower_pos] + K):
        i += 1

    num_transmitters += 1

print (num_transmitters)

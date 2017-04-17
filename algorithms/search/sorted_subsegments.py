N, Q, K = map(int, input().split(" "))
arr = list([int(x) for x in input().split(" ")])

sorts = []
for _ in range(Q):
    low, up = map(int, input().split(" "))

    if low != up:
        sorts.append([low, up])

min_k = K
max_k = K

useful_sorts = []
for segment in reversed(sorts):

    if min_k <= segment[0] <= max_k or min_k <= segment[1] <= max_k:
        min_k = min(min_k, segment[0])
        max_k = max(max_k, segment[1])
        useful_sorts.insert(0, segment)

for segment in sorts:
    low, up = segment
    arr = arr[:low] + sorted(arr[low:up + 1]) + arr[up+1 : ]

print (arr[K])

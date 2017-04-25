def insert_sort(arr, trace=True):
    rightmost = arr[-1]
    arr[-1] = arr[-2]

    n = len(arr)
    i = n - 2
    while i >= 0 and rightmost < arr[i]:
        arr[i + 1] = arr[i]
        if trace:
            print(" ".join(map(str, arr)))
        i -= 1

    arr[i + 1] = rightmost
    if trace:
        print(" ".join(map(str, arr)))

input()
arr = [int(x) for x in input().split(" ")]
insert_sort(arr)

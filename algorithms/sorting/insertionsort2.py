def insert_sort(arr, trace=True):
    n = len(arr)
    for i in range(1, n):
        j = i
        while(j > 0 and arr[j] < arr[j - 1]):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

        if trace:
            print(" ".join(map(str, arr)))

_ = input()
arr = [int(x) for x in input().split(" ")]
insert_sort(arr)

def quicksort(arr):
    if len(arr) > 1:
        pivot = arr[0]
        equal = list(filter(lambda x: x == pivot, arr))
        left = list(filter(lambda x: x < pivot, arr))
        right = list(filter(lambda x: x > pivot, arr))

        return quicksort(left) + equal + quicksort(right)
    return arr

_ = input()
arr = [int(x) for x in input().split(" ")]
print(" ".join(map(str, quicksort(arr))))

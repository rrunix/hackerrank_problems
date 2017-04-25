def quicksort(arr):
    if len(arr) > 1:

        pivot = arr[0]
        equal = list(filter(lambda x: x == pivot, arr))
        left = list(filter(lambda x: x < pivot, arr))
        right = list(filter(lambda x: x > pivot, arr))

        if len(left) > 1:
            left = quicksort(left)
            print(" ".join(map(str, left)))

        if len(right) > 1:
            right = quicksort(right)
            print(" ".join(map(str, right)))

        return left + equal + right
    return arr

_ = input()
arr = [int(x) for x in input().split(" ")]
print(" ".join(map(str, quicksort(arr))))

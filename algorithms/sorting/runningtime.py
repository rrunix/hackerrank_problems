def insertion_sort(arr):
    iterations = 0
    for i in range(1, len(arr)):
        j = i
        while(j > 0 and arr[j] < arr[j - 1]):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            iterations += 1
            j -= 1

    return iterations


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
print(insertion_sort(ar))

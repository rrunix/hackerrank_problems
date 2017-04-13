#Source: https://www.hackerrank.com/challenges/playing-with-numbers
from itertools import accumulate
from bisect import bisect_right, bisect_left

N = int(input())

arr = [int(x) for x in input().split(" ")]
arr = sorted(arr)

pos_pivot = bisect_left(arr, 0)

arr_neg = arr[:pos_pivot]
arr_pos = arr[pos_pivot:]

sum_arr_neg = list(accumulate(arr_neg[::-1]))
sum_arr_pos = list(accumulate(arr_pos))

len_pos = len(arr_pos)
len_neg = len(arr_neg)

sum_pos = sum_arr_pos[-1] if len_pos > 0 else 0
sum_neg = sum_arr_neg[-1] if len_neg > 0 else 0

Q = int(input())

query_acc = 0
queries = [int(x) for x in input().split(" ")]

for query in queries:
    query_acc += query

    if query_acc > 0:
        pivot_left = bisect_left(arr_neg, -query_acc)

        # Positive side
        res = sum_pos + len_pos * query_acc

        # Negative to positive
        neg_overlap = 0 if pivot_left == len_neg else sum_arr_neg[len_neg - pivot_left - 1]
        res += neg_overlap + (len_neg - pivot_left) * query_acc

        # Yet negative
        res += -1 * (sum_neg - neg_overlap) - (pivot_left) * query_acc

    elif query_acc < 0:
        pivot_right = bisect_right(arr_pos, -query_acc)

        # Negative side
        res = -1 * (sum_neg + len_neg * query_acc)

        # Positive to negative
        pos_overlap = 0 if pivot_right == 0 else sum_arr_pos[pivot_right - 1]
        res += -1 * pivot_right * query_acc - pos_overlap

        # Yet positive
        res += sum_pos - pos_overlap + (len_pos - pivot_right) * query_acc
    else:
        res = sum_pos + -1 * sum_neg

    print(res)

#source https://www.hackerrank.com/challenges/maximum-subarray-sum
from itertools import accumulate
import bisect

for _ in range(int(input())):
    n, m = list(map(int, input().split(' ')))

    numbers = list(map(lambda x: int(x) % m, input().split(' ')))
    preffix_sum = list(map(lambda x: x % m, accumulate(numbers)))

    #Larger number in the array
    max_sum = max(preffix_sum)


    #Keep track of the previous elements of the current element in the preffix sum.
    #If we have a value x1 in the previous list and the current element is x2, then
    #the difference between them is (x2 - x1) % m. Since we know that x1 has appear
    #before x2, then (x1, x2) is a valid subarray.

    #So the problem is reduced to maximize the expression (x2 - x1) % m, which
    #is maximized when x1 < x2 and the value of x1 is close to x2.
    #(This is a bisect_right operation, which runs in O(log(n))).

    #(The case of x2 > 0 and x1 = 0 is tackled down above by finding
    #the larger number)
    previous = []
    for i, x in enumerate(preffix_sum):
        j = bisect.bisect_right(previous, x)

        #Check if there is a value lower than x in the previous values
        if j != i:
            max_sum = max(max_sum, (preffix_sum[i] - previous[j]) % m)
        previous.insert(j, x)

    print (max_sum)

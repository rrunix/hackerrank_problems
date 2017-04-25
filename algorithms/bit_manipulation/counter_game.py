#source https://www.hackerrank.com/challenges/counter-game
import math

T = int(input())

for _ in range(T):
    print (["Richard", "Louise"][(bin(int(input())-1).count('1') % 2)])

    """
        We can not simple take the log2 and then apply the modulus because in numbers
        which has 0s in its binary representation it will not works
        (well.. the number of zeros can be even and compensate each other..)


        1000 - 1 = 0111 -> 3 ones : 3 moves
        1001 - 1 = 1000 -> 1 one  : 1 move only

    """

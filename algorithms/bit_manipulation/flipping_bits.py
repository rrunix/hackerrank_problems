#source https://www.hackerrank.com/challenges/flipping-bits
N = int(input())

for _ in range(N):
    #Get the binary representation and fit to 32 bits
    bin_rep = bin(int(input()))[2:].zfill(32)
    #Change 0s by 1s
    print (int(bin_rep.replace('0', '2').replace('1','0').replace('2', '1'), 2))

    """
        Would be easier with 32 bit integers (applying ~)
    """

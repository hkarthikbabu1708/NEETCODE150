# You are given an unsigned integer n. Return the number of 1 bits in its binary representation.

def hammingWeight(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# n = 0o00000000000000000000000000010111 (leading zeros are not allowed in python, for octal numbers prefix 0o
n = 0o01111111111111111111111111111101
print(hammingWeight(n))
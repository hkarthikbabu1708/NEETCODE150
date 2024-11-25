# Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.

def reverseBits(n):
    result = 0
    for i in range(32):
        bit = n & 1
        result = result << 1 | bit
        n >>= 1
    return result


n = 0o00000000000000000000000000010101
print(reverseBits(n))
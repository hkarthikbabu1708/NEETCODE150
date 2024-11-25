# Given two integers a and b, return the sum of the two integers without using the + and - operators.

def getSum(a, b):
    MASK = 0xFFFFFFFF
    MAX_INT = 0x7FFFFFFF

    while b != 0:
        sum_on_carry = (a ^ b) & MASK
        carry = ((a & b) << 1) & MASK
        a, b = sum_on_carry, carry
    return a if a <= MAX_INT else ~(a ^ MASK)

a = 1
b = 1
print(getSum(a,b))
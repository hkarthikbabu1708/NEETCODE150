# You are given a signed 32-bit integer x.
# Return x after reversing each of its digits.
# After reversing, if x goes outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0 instead.

def reverse(x):
    res = 0
    is_neg = x < 0
    x = abs(x)

    while x != 0:
        digit = x % 10
        res = res * 10 + digit
        x = x // 10

    if res < (-2**31) or res > (2**31):
        return 0

    if is_neg:
        return -res

    return res


x = 1234
print(reverse(x))
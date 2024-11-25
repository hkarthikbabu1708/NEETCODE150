# Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].
# Return an array output where output[i] is the number of 1's in the binary representation of i.

#brte force approach
# def countBits(n):
#     res = []
#     for i in range(n+1):
#         res.append(bin(i).count('1'))
#     return res

def countBits(n):
    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = dp[i>>1] + i & 1
    return dp

n = 4
print(countBits(n))

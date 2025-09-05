def minimumOperations(num1: int, num2: int) -> int:
    for k in range(1, 61):  
        S = num1 - k * num2
        if S >= k and S.bit_count() <= k:
            return k
    return -1

"""
After k operations, the total subtracted is:
    sum(2^i_j + num2) = (sum of chosen powers of 2) + k * num2

Thus the condition is:
    num1 = (sum of some powers of 2) + k * num2

Let S = num1 - k * num2.
Then:
    - S must be representable as the sum of k powers of 2.
    - Minimum requirements:
        1) S >= k  (since the smallest k powers of 2 sum is k*1 = k)
        2) popcount(S) <= k  (binary 1-bits must fit within k choices)
"""
class Solution:
    def myPow(self, x, n):
        base = 1
        if n == 0:
            return 1
        elif n < 0:
            x = 1/x
            n = -n
        current = x
        k = n
        while k > 0:
            if k%2 == 1:
                base *= current
            current *= current
            k = k // 2
        return base
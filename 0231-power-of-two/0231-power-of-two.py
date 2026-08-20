class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1
        while x <= n:
            if x == n:
                return True
            if x > 2 ** 30:
                break
            x = x << 1
        return False